package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.SessionNotFoundError
import java.lang.Exception


/** 결제 세션이 존재하지 않는 경우 */
public class SessionNotFoundException internal constructor(
  cause: SessionNotFoundError
) : PortOneException(cause.message), ClosePaymentSessionException, GetPaymentSessionException {
}
