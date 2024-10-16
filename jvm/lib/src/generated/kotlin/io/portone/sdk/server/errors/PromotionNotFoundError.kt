package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.GetPromotionError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 프로모션이 존재하지 않는 경우 */
@Serializable
@SerialName("PROMOTION_NOT_FOUND")
@ConsistentCopyVisibility
public data class PromotionNotFoundError internal constructor(
  override val message: String? = null,
): GetPromotionError
