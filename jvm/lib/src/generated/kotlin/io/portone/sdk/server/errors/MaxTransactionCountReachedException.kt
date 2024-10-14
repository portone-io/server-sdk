package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.MaxTransactionCountReachedError
import java.lang.Exception


/** 결제 혹은 본인인증 시도 횟수가 최대에 도달한 경우 */
public class MaxTransactionCountReachedException(
  cause: MaxTransactionCountReachedError
) : Exception(cause.message) {
}
