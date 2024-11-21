package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.SumOfPartsExceedsCancelAmountError
import java.lang.Exception


/** 면세 금액 등 하위 항목들의 합이 전체 취소 금액을 초과한 경우 */
public class SumOfPartsExceedsCancelAmountException internal constructor(
  cause: SumOfPartsExceedsCancelAmountError
) : PortOneException(cause.message), CancelPaymentException {
}
