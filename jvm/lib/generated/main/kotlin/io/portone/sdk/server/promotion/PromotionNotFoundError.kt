package io.portone.sdk.server.promotion

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 프로모션이 존재하지 않는 경우 */
@Serializable
@SerialName("PROMOTION_NOT_FOUND")
public data class PromotionNotFoundError(
  override val message: String? = null,
): GetPromotionError,
