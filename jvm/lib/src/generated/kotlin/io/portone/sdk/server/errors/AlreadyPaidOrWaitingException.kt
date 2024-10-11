package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.AlreadyPaidOrWaitingError
import java.lang.Exception


/** 결제가 이미 완료되었거나 대기중인 경우 */
public class AlreadyPaidOrWaitingException(
  cause: AlreadyPaidOrWaitingError
) : Exception(cause.message) {
}
