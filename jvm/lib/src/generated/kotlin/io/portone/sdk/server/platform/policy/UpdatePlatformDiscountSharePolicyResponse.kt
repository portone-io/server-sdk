package io.portone.sdk.server.platform.policy

import io.portone.sdk.server.platform.PlatformDiscountSharePolicy
import kotlinx.serialization.Serializable

/** 할인 분담 정책 업데이트 성공 응답 */
@Serializable
public data class UpdatePlatformDiscountSharePolicyResponse(
  /** 업데이트된 할인 분담 정책 */
  val discountSharePolicy: PlatformDiscountSharePolicy,
)
