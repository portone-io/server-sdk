package io.portone.sdk.server.errors

import io.portone.sdk.server.payment.PromotionPayMethodDoesNotMatchError
import java.lang.Exception


/** 결제수단이 프로모션에 지정된 것과 일치하지 않는 경우 */
public class PromotionPayMethodDoesNotMatchException(
  cause: PromotionPayMethodDoesNotMatchError
) : Exception(cause.message) {
}
