package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PromotionDiscountRetainOptionShouldNotBeChangedError
import java.lang.Exception


/** 프로모션 혜택 유지 옵션을 이전 부분 취소와 다른 것으로 입력한 경우 */
public class PromotionDiscountRetainOptionShouldNotBeChangedException(
  cause: PromotionDiscountRetainOptionShouldNotBeChangedError
) : Exception(cause.message) {
}
