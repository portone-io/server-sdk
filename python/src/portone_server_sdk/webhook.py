import codecs
import hmac
import time
from collections.abc import Mapping
from dataclasses import dataclass, field
from typing import Literal, Optional, Union

from portone_server_sdk.errors import PortOneError

_required_headers = {
    "webhook-id": str,
    "webhook-timestamp": str,
    "webhook-signature": str,
}

WebhookVerificationFailureReason = Literal[
    "MISSING_REQUIRED_HEADERS",
    "NO_MATCHING_SIGNATURE",
    "INVALID_SIGNATURE",
    "TIMESTAMP_TOO_OLD",
    "TIMESTAMP_TOO_NEW",
]
"""웹훅 검증 실패 사유입니다.

:obj:`WebhookVerificationError.get_message` 에 전달하여 에러 메시지를 얻을 수 있습니다.
"""


@dataclass
class WebhookVerificationError(PortOneError):
    """웹훅 검증이 실패했을 경우"""

    message: Optional[str] = field(init=False)
    reason: WebhookVerificationFailureReason

    def __post_init__(self) -> None:
        self.message = self.get_message(self.reason)

    @classmethod
    def get_message(cls, reason: WebhookVerificationFailureReason) -> str:
        """웹훅 검증 실패 사유로부터 에러 메시지를 생성합니다.

        Args:
            reason (WebhookVerificationFailureReason): 에러 메시지를 생성할 실패 사유.

        Returns:
            str: 에러 메시지.
        """
        if reason == "MISSING_REQUIRED_HEADERS":
            return "필수 헤더가 누락되었습니다."
        elif reason == "NO_MATCHING_SIGNATURE":
            return "올바른 웹훅 시그니처를 찾을 수 없습니다."
        elif reason == "INVALID_SIGNATURE":
            return "웹훅 시그니처가 유효하지 않습니다."
        elif reason == "TIMESTAMP_TOO_OLD":
            return "웹훅 시그니처의 타임스탬프가 만료 기한을 초과했습니다."
        elif reason == "TIMESTAMP_TOO_NEW":
            return "웹훅 시그니처의 타임스탬프가 미래 시간으로 설정되어 있습니다."


@dataclass
class InvalidInputError(PortOneError):
    """SDK에 전달한 사용자 입력이 잘못되었을 경우"""

    message: Optional[str]


def verify(
    secret: Union[str, bytes, bytearray], payload: str, headers: Mapping[str, str]
) -> None:
    """웹훅 페이로드를 검증합니다.

    Args:
        secret (str | bytes | bytearray): 웹훅 시크릿
        payload (str): 웹훅 페이로드
        headers (Mapping[str, str]): 웹훅 요청 시 포함된 헤더

    Raises:
        InvalidInputError: 입력받은 시크릿이 유효하지 않을 때 발생합니다.
        WebhookVerificationError: 웹훅 검증에 실패했을 때 발생합니다.
    """
    for header_name in _required_headers:
        header_value = headers.get(header_name)
        if not isinstance(header_value, _required_headers[header_name]):
            raise WebhookVerificationError("MISSING_REQUIRED_HEADERS")

    msg_timestamp = headers["webhook-timestamp"]
    _verify_timestamp(msg_timestamp)

    msg_id = headers["webhook-id"]
    expected_signature = _sign(secret, msg_id, msg_timestamp, payload)

    msg_signature = headers["webhook-signature"]
    for versioned_signagure in msg_signature.split(" "):
        split = versioned_signagure.split(",", 3)
        if len(split) < 2:
            continue
        version, signature, *_ = split
        if version != "v1":
            continue
        try:
            signature_decoded = codecs.decode(signature.encode(), "base64")
        except ValueError:
            continue

        if hmac.compare_digest(signature_decoded, expected_signature):
            return
    raise WebhookVerificationError("NO_MATCHING_SIGNATURE")


WEBHOOK_TOLERANCE_IN_SECONDS = 5 * 60  # 5분


def _verify_timestamp(timestamp_header: str) -> None:
    now = int(time.time())
    try:
        timestamp = int(timestamp_header)
    except ValueError:
        raise WebhookVerificationError("INVALID_SIGNATURE")
    if now - timestamp > WEBHOOK_TOLERANCE_IN_SECONDS:
        raise WebhookVerificationError("TIMESTAMP_TOO_OLD")
    if timestamp > now + WEBHOOK_TOLERANCE_IN_SECONDS:
        raise WebhookVerificationError("TIMESTAMP_TOO_NEW")


def _sign(
    secret: Union[str, bytes, bytearray], msg_id: str, msg_timestamp: str, payload: str
) -> bytes:
    raw_secret = _get_raw_secret(secret)
    to_sign = f"{msg_id}.{msg_timestamp}.{payload}"
    return hmac.digest(raw_secret, to_sign.encode(), "sha256")


_prefix = "whsec_"


def _get_raw_secret(secret: Union[str, bytes, bytearray]) -> Union[bytes, bytearray]:
    if isinstance(secret, (bytes, bytearray)):
        raw_secret = secret
    elif isinstance(secret, str):
        secret_base64 = secret[len(_prefix) :] if secret.startswith(_prefix) else secret
        try:
            raw_secret = codecs.decode(secret_base64.encode(), "base64")
        except ValueError:
            raise InvalidInputError(
                "`secret` 파라미터가 올바른 Base64 문자열이 아닙니다."
            )
    else:
        raise InvalidInputError("`secret` 파라미터의 타입이 잘못되었습니다.")

    if len(raw_secret) == 0:
        raise InvalidInputError("시크릿은 비어 있을 수 없습니다.")

    return raw_secret


__all__ = [
    "WebhookVerificationFailureReason",
    "WebhookVerificationError",
    "InvalidInputError",
    "verify",
]