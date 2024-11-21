package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError
import java.lang.Exception


/** 취소 면세 금액이 취소 가능한 면세 금액을 초과한 경우 */
public class CancelTaxFreeAmountExceedsCancellableTaxFreeAmountException internal constructor(
  cause: CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError
) : PortOneException(cause.message), CancelPaymentException {
}
