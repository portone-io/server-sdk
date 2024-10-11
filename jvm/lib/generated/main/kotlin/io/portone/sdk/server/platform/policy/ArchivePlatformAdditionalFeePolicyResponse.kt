package io.portone.sdk.server.platform.policy

import io.portone.sdk.server.platform.PlatformAdditionalFeePolicy
import kotlinx.serialization.Serializable

/** 추가 수수료 정책 보관 성공 응답 */
@Serializable
public data class ArchivePlatformAdditionalFeePolicyResponse(
  /** 보관된 추가 수수료 정책 */
  val additionalFeePolicy: PlatformAdditionalFeePolicy,
)
