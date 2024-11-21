package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.NegativePromotionAdjustedCancelAmountError
import java.lang.Exception


/** 프로모션에 의해 조정된 취소 금액이 음수인 경우 */
public class NegativePromotionAdjustedCancelAmountException internal constructor(
  cause: NegativePromotionAdjustedCancelAmountError
) : PortOneException(cause.message), CancelPaymentException {
}
