package io.portone.sdk.server.errors

import io.portone.sdk.server.payment.CancelAmountExceedsCancellableAmountError
import java.lang.Exception


/** 결제 취소 금액이 취소 가능 금액을 초과한 경우 */
public class CancelAmountExceedsCancellableAmountException(
  cause: CancelAmountExceedsCancellableAmountError
) : Exception(cause.message) {
}
