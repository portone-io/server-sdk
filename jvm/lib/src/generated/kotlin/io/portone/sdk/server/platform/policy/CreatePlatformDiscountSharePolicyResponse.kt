package io.portone.sdk.server.platform.policy

import io.portone.sdk.server.platform.PlatformDiscountSharePolicy
import kotlinx.serialization.Serializable

/** 할인 분담 정책 생성 성공 응답 */
@Serializable
public data class CreatePlatformDiscountSharePolicyResponse(
  /** 생성된 할인 분담 정책 */
  val discountSharePolicy: PlatformDiscountSharePolicy,
)


