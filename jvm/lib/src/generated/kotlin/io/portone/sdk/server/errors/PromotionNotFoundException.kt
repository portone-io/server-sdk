package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PromotionNotFoundError
import java.lang.Exception


/** 프로모션이 존재하지 않는 경우 */
public class PromotionNotFoundException(
  cause: PromotionNotFoundError
) : Exception(cause.message) {
}
