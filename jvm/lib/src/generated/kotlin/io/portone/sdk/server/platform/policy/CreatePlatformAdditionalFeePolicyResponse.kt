package io.portone.sdk.server.platform.policy

import io.portone.sdk.server.platform.PlatformAdditionalFeePolicy
import kotlinx.serialization.Serializable

/** 플랫폼 생성 성공 응답 정보 */
@Serializable
public data class CreatePlatformAdditionalFeePolicyResponse(
  /** 생성된 추가 수수료 정책 */
  val additionalFeePolicy: PlatformAdditionalFeePolicy,
)


