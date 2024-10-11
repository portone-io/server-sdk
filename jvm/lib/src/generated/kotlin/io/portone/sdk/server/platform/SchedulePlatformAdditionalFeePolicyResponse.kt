package io.portone.sdk.server.platform

import io.portone.sdk.server.platform.PlatformAdditionalFeePolicy
import kotlinx.serialization.Serializable

/** 추가 수수료 정책 업데이트 예약 성공 응답 */
@Serializable
public data class SchedulePlatformAdditionalFeePolicyResponse(
  /** 예약된 추가 수수료 정책 */
  val scheduledAdditionalFeePolicy: PlatformAdditionalFeePolicy,
)
