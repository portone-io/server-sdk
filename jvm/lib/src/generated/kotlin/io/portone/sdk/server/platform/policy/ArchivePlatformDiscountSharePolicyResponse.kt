package io.portone.sdk.server.platform.policy

import io.portone.sdk.server.platform.PlatformDiscountSharePolicy
import kotlinx.serialization.Serializable

/** 할인 분담 보관 성공 응답 */
@Serializable
public data class ArchivePlatformDiscountSharePolicyResponse(
  /** 보관된 할인 분담 */
  val discountSharePolicy: PlatformDiscountSharePolicy,
)
