package io.portone.sdk.server.errors

import io.portone.sdk.server.payment.CancelTaxAmountExceedsCancellableTaxAmountError
import java.lang.Exception


/** 취소 과세 금액이 취소 가능한 과세 금액을 초과한 경우 */
public class CancelTaxAmountExceedsCancellableTaxAmountException(
  cause: CancelTaxAmountExceedsCancellableTaxAmountError
) : Exception(cause.message) {
}
