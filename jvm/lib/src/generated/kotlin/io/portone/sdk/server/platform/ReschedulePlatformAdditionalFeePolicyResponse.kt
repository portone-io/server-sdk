package io.portone.sdk.server.platform

import io.portone.sdk.server.platform.PlatformAdditionalFeePolicy
import kotlinx.serialization.Serializable

/** 추가 수수료 정책 예약 업데이트 재설정 성공 응답 */
@Serializable
public data class ReschedulePlatformAdditionalFeePolicyResponse(
  /** 예약된 추가 수수료 정책 */
  val scheduledAdditionalFeePolicy: PlatformAdditionalFeePolicy,
)
