package io.portone.sdk.server.platform.policy

import io.portone.sdk.server.platform.PlatformAdditionalFeePolicy
import kotlinx.serialization.Serializable

/** 추가 수수료 정책 업데이트 성공 응답 */
@Serializable
public data class UpdatePlatformAdditionalFeePolicyResponse(
  /** 업데이트된 추가 수수료 정책 */
  val additionalFeePolicy: PlatformAdditionalFeePolicy,
)
