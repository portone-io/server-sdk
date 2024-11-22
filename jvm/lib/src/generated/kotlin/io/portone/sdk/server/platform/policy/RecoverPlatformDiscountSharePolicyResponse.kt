package io.portone.sdk.server.platform.policy

import io.portone.sdk.server.platform.PlatformDiscountSharePolicy
import kotlinx.serialization.Serializable

/** 할인 분담 복원 성공 응답 */
@Serializable
public data class RecoverPlatformDiscountSharePolicyResponse(
  /** 복원된 할인 분담 */
  val discountSharePolicy: PlatformDiscountSharePolicy,
)


