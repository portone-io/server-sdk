package io.portone.sdk.server.platform

import io.portone.sdk.server.platform.UpdatePlatformAdditionalFeePolicyBody
import kotlinx.datetime.Instant
import kotlinx.serialization.Serializable

/** 추가 수수료 정책 예약 업데이트 재설정을 위한 입력 정보 */
@Serializable
public data class ReschedulePlatformAdditionalFeePolicyBody(
  /** 반영할 업데이트 내용 */
  val update: UpdatePlatformAdditionalFeePolicyBody,
  /** 업데이트 적용 시점 */
  val appliedAt: Instant,
)
