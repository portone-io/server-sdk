import codecs
import hmac
import json
import time
from dataclasses import dataclass
from typing import Optional

import portone_server_sdk as portone

secret = codecs.decode(b"pzQGE83cSIRKM4/WH5QY+g==", "base64")

test_object_recognized = {
    "type": "Transaction.Cancelled",
    "timestamp": "2024-04-25T10:00:00.000Z",
    "data": {
        "paymentId": "example-payment-id",
        "transactionId": "55451513-9763-4a7a-bb43-78a4c65be843",
        "cancellationId": "0cdd91e9-4e7c-44a3-a72e-1a6511826c2b",
        "storeId": "store-ae356798-3d20-4969-b739-14c6b0e1a667",
    },
}

test_object_unrecognized = {"test": "test payload"}


@dataclass
class WebhookMock:
    headers: dict[str, str]
    payload: str


def make_webhook(object: dict, epoch_second: Optional[int] = None) -> WebhookMock:
    if epoch_second is None:
        epoch_second = int(time.time())
    webhook_id = "dummy-webhook-id"
    payload = json.dumps(object)
    plaintext = f"{webhook_id}.{epoch_second}.{payload}".encode()
    signature = (
        codecs.encode(
            hmac.digest(secret, plaintext, "sha256"),
            "base64",
        )
        .strip()
        .decode()
    )
    return WebhookMock(
        {
            "webhook-id": webhook_id,
            "webhook-signature": f"v1,{signature}",
            "webhook-timestamp": str(epoch_second),
        },
        payload,
    )


def test_verify_valid_signature_unrecognized():
    test_webhook = make_webhook(test_object_unrecognized)
    webhook = portone.webhook.verify(secret, test_webhook.payload, test_webhook.headers)
    assert webhook == test_object_unrecognized


def test_verify_valid_signature_recognized():
    test_webhook = make_webhook(test_object_recognized)
    webhook = portone.webhook.verify(secret, test_webhook.payload, test_webhook.headers)
    assert isinstance(webhook, portone.webhook.WebhookTransactionCancelledCancelled)


def test_verify_multiple_signatures():
    test_webhook = make_webhook(test_object_unrecognized)
    sigs = [
        "v1,Ceo5qEr07ixe2NLpvHk3FH9bwy/WavXrAFQ/9tdO6mc=",
        "v2,Ceo5qEr07ixe2NLpvHk3FH9bwy/WavXrAFQ/9tdO6mc=",
        test_webhook.headers["webhook-signature"],
        "v1,Ceo5qEr07ixe2NLpvHk3FH9bwy/WavXrAFQ/9tdO6mc=",
    ]
    test_webhook.headers["webhook-signature"] = " ".join(sigs)
    webhook = portone.webhook.verify(secret, test_webhook.payload, test_webhook.headers)
    assert webhook == test_object_unrecognized
