package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.MaxCancelCountReachedError
import java.lang.Exception


/** 취소 시도 횟수가 초과된 경우 */
public class MaxCancelCountReachedException internal constructor(
  cause: MaxCancelCountReachedError
) : PortOneException(cause.message), CancelPaymentException {
}
