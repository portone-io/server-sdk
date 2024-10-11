package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.CancellableAmountConsistencyBrokenError
import java.lang.Exception


/** 취소 가능 잔액 검증에 실패한 경우 */
public class CancellableAmountConsistencyBrokenException(
  cause: CancellableAmountConsistencyBrokenError
) : Exception(cause.message) {
}
