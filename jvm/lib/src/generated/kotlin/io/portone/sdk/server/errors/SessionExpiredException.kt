package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.SessionExpiredError
import java.lang.Exception


/** 결제 세션이 만료된 경우 */
public class SessionExpiredException internal constructor(
  cause: SessionExpiredError
) : PortOneException(cause.message), GetPaymentSessionException {
}
