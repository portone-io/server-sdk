package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.DiscountAmountExceedsTotalAmountError
import java.lang.Exception


/** 프로모션 할인 금액이 결제 시도 금액 이상인 경우 */
public class DiscountAmountExceedsTotalAmountException(
  cause: DiscountAmountExceedsTotalAmountError
) : Exception(cause.message) {
}
