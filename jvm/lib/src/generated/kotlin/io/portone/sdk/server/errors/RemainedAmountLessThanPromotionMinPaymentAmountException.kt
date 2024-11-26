package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.RemainedAmountLessThanPromotionMinPaymentAmountError
import java.lang.Exception


/** 부분 취소 시, 취소하게 될 경우 남은 금액이 프로모션의 최소 결제 금액보다 작아지는 경우 */
public class RemainedAmountLessThanPromotionMinPaymentAmountException internal constructor(
  cause: RemainedAmountLessThanPromotionMinPaymentAmountError
) : PortOneException(cause.message), CancelPaymentException {
}
