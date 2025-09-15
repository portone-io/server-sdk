package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.InvalidPaymentTokenError
import java.lang.Exception


/** 유효하지 않은 결제 토큰인 경우 */
public class InvalidPaymentTokenException internal constructor(
  cause: InvalidPaymentTokenError
) : PortOneException(cause.message), ConfirmPaymentException {
}
