import asyncio
import json
from unittest.mock import AsyncMock

import httpx
import pytest

from portone_server_sdk import PaymentClient
from portone_server_sdk.common import PageInput
from portone_server_sdk.errors import (
    PaymentAlreadyCancelledError,
    PaymentNotFoundError,
    UnknownError,
)
from portone_server_sdk.payment import CancelledPayment, GetPaymentsResponse


@pytest.fixture
def mock_client():
    requests = []
    response = {"status": 200, "json": {}}

    def handler(request):
        requests.append(request)
        return httpx.Response(response["status"], json=response["json"])

    clients = []

    def make_client(store_id=None):
        client = PaymentClient(
            secret="test-secret", base_url="https://api.portone.io", store_id=store_id
        )
        client._sync_client.close()
        client._sync_client = httpx.Client(transport=httpx.MockTransport(handler))
        clients.append(client)
        return client

    yield make_client, requests, response
    for client in clients:
        client._sync_client.close()


def assert_request(request, method, raw_path, body=b""):
    assert request.method == method
    assert request.url.raw_path == raw_path
    assert request.content == body
    assert request.headers["Authorization"] == "PortOne test-secret"
    assert request.headers["User-Agent"]


def test_get_payments_without_params(mock_client):
    make_client, requests, response = mock_client
    response["json"] = {"items": [], "page": {"number": 0, "size": 0, "totalCount": 0}}
    payments = make_client().get_payments()
    assert isinstance(payments, GetPaymentsResponse)
    assert_request(requests[0], "GET", b"/payments?requestBody=%7B%7D")


@pytest.mark.parametrize(
    ("body", "error_class"),
    [
        ("private-body", ValueError),
        ({"private-body": 1}, KeyError),
        ({"items": "private-body"}, ValueError),
    ],
)
def test_invalid_response_messages_omit_body(mock_client, body, error_class):
    make_client, _, response = mock_client
    response["json"] = body
    with pytest.raises(error_class) as caught:
        make_client().get_payments()
    assert "private-body" not in str(caught.value)


def test_unknown_error_keeps_body_out_of_message(mock_client):
    make_client, _, response = mock_client
    response.update(status=502, json={"detail": "private-body"})
    with pytest.raises(UnknownError) as caught:
        make_client().get_payments()
    assert str(caught.value) == caught.value.message
    assert "private-body" not in repr(caught.value)
    assert caught.value.error == response["json"]


def test_get_payments_with_params(mock_client):
    make_client, requests, response = mock_client
    response["json"] = {"items": [], "page": {"number": 0, "size": 0, "totalCount": 0}}
    payments = make_client().get_payments(page=PageInput(3000))
    assert len(payments.items) == 0
    assert_request(
        requests[0],
        "GET",
        b"/payments?requestBody=%7B%22page%22%3A+%7B%22number%22%3A+3000%7D%7D",
    )
    assert json.loads(requests[0].url.params["requestBody"]) == {
        "page": {"number": 3000}
    }


def test_get_payment_with_params(mock_client):
    make_client, requests, response = mock_client
    timestamp = "2024-01-01T00:00:00Z"
    response["json"] = {
        "status": "CANCELLED",
        "id": "test-server-sdk",
        "transactionId": "tx",
        "merchantId": "merchant",
        "storeId": "store",
        "channel": {"type": "TEST", "pgProvider": "INICIS", "pgMerchantId": "merchant"},
        "version": "V2",
        "requestedAt": timestamp,
        "updatedAt": timestamp,
        "statusChangedAt": timestamp,
        "orderName": "order",
        "amount": {
            "total": 100,
            "taxFree": 0,
            "discount": 0,
            "paid": 100,
            "cancelled": 100,
            "cancelledTaxFree": 0,
        },
        "currency": "KRW",
        "customer": {},
        "origin": {"platformType": "API", "ipAddress": "127.0.0.1"},
        "cancellations": [
            {
                "status": "SUCCEEDED",
                "id": "cancel-id",
                "totalAmount": 100,
                "taxFreeAmount": 0,
                "vatAmount": 0,
                "reason": "test",
                "requestedAt": timestamp,
            }
        ],
        "cancelledAt": timestamp,
    }
    payment = make_client().get_payment(payment_id="test-server-sdk")
    assert_request(requests[0], "GET", b"/payments/test-server-sdk")
    assert isinstance(payment, CancelledPayment)
    assert payment.id == "test-server-sdk"
    assert payment.amount.total == 100
    assert payment.cancellations[0].id == "cancel-id"
    assert payment.cancellations[0].reason == "test"


def test_get_payment_rejects_dot_segments_before_sending(mock_client, monkeypatch):
    make_client, requests, _ = mock_client
    client = make_client()
    async_request = AsyncMock()
    monkeypatch.setattr(client._async_client, "request", async_request)
    for payment_id in (".", ".."):
        with pytest.raises(ValueError, match="dot segments"):
            client.get_payment(payment_id=payment_id)
        with pytest.raises(ValueError, match="dot segments"):
            asyncio.run(client.get_payment_async(payment_id=payment_id))
    assert requests == []
    async_request.assert_not_called()


@pytest.mark.parametrize(
    ("payment_id", "path"),
    [
        (" ", b"/payments/%20"),
        ("order.v2/part", b"/payments/order.v2%2Fpart"),
        (b"order/\xff", b"/payments/order%2F%FF"),
        (bytearray(b"order/part"), b"/payments/order%2Fpart"),
        ("...", b"/payments/..."),
        ("%2E", b"/payments/%252E"),
        (".%2e", b"/payments/.%252e"),
        ("%2E%2e", b"/payments/%252E%252e"),
    ],
)
def test_get_payment_preserves_path_parameter(mock_client, payment_id, path):
    make_client, requests, response = mock_client
    response.update(
        status=404, json={"type": "PAYMENT_NOT_FOUND", "message": "not found"}
    )
    with pytest.raises(PaymentNotFoundError) as caught:
        make_client().get_payment(payment_id=payment_id)
    assert str(caught.value) == "not found"
    assert_request(requests[0], "GET", path)


def test_get_cancel_payment_with_already_cancelled_payment_id(mock_client):
    make_client, requests, response = mock_client
    response.update(
        status=409,
        json={"type": "PAYMENT_ALREADY_CANCELLED", "message": "already cancelled"},
    )
    with pytest.raises(PaymentAlreadyCancelledError):
        make_client().cancel_payment(
            payment_id="test-server-sdk", reason="test", amount=1
        )
    assert_request(
        requests[0],
        "POST",
        b"/payments/test-server-sdk/cancel",
        b'{"amount":1,"reason":"test"}',
    )
    assert json.loads(requests[0].content) == {"amount": 1, "reason": "test"}


def test_store_id_is_serialized(mock_client):
    make_client, requests, response = mock_client
    response.update(
        status=404, json={"type": "PAYMENT_NOT_FOUND", "message": "not found"}
    )
    with pytest.raises(PaymentNotFoundError):
        make_client(store_id="store-id").get_payment(payment_id="test-server-sdk")
    assert_request(requests[0], "GET", b"/payments/test-server-sdk?storeId=store-id")
