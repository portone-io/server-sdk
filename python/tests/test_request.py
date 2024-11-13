import os

import pytest

import portone_server_sdk as sdk
from portone_server_sdk import PortOneClient

PORTONE_API_SECRET: str = os.environ["PORTONE_API_SECRET"]

client = PortOneClient(secret=PORTONE_API_SECRET)


def test_get_payments_without_params():
    payments = client.payment.get_payments()
    assert isinstance(payments, sdk.payment.GetPaymentsResponse)


def test_get_payments_with_params():
    payments = client.payment.get_payments(page=sdk.common.PageInput(3000))
    assert len(payments.items) == 0


def test_get_payment_with_params():
    payment = client.payment.get_payment(payment_id="test-server-sdk")
    assert isinstance(payment, sdk.payment.CancelledPayment)


def test_get_payment_with_invalid_payment_id():
    with pytest.raises(sdk.errors.PaymentNotFoundError):
        client.payment.get_payment(payment_id=" ")


def test_get_cancel_payment_with_already_cancelled_payment_id():
    with pytest.raises(sdk.errors.PaymentAlreadyCancelledError):
        client.payment.cancel_payment(
            payment_id="test-server-sdk", reason="test", amount=1
        )
