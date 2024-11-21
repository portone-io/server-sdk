package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PromotionNotFoundError
import java.lang.Exception


/** 프로모션이 존재하지 않는 경우 */
public class PromotionNotFoundException internal constructor(
  cause: PromotionNotFoundError
) : PortOneException(cause.message), GetPromotionException {
}
