import os

import pytest

from portone_server_sdk import PaymentClient
from portone_server_sdk.common import PageInput
from portone_server_sdk.errors import PaymentAlreadyCancelledError, PaymentNotFoundError
from portone_server_sdk.payment import CancelledPayment, GetPaymentsResponse

PORTONE_API_SECRET: str = os.environ["PORTONE_API_SECRET"]

client = PaymentClient(secret=PORTONE_API_SECRET)


def test_get_payments_without_params():
    payments = client.get_payments()
    assert isinstance(payments, GetPaymentsResponse)


def test_get_payments_with_params():
    payments = client.get_payments(page=PageInput(3000))
    assert len(payments.items) == 0


def test_get_payment_with_params():
    payment = client.get_payment(payment_id="test-server-sdk")
    assert isinstance(payment, CancelledPayment)


def test_get_payment_with_invalid_payment_id():
    with pytest.raises(PaymentNotFoundError):
        client.get_payment(payment_id=" ")


def test_get_cancel_payment_with_already_cancelled_payment_id():
    with pytest.raises(PaymentAlreadyCancelledError):
        client.cancel_payment(payment_id="test-server-sdk", reason="test", amount=1)
