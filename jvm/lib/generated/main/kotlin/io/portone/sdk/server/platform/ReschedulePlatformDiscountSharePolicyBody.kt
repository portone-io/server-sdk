package io.portone.sdk.server.platform

import io.portone.sdk.server.platform.UpdatePlatformDiscountSharePolicyBody
import kotlinx.datetime.Instant
import kotlinx.serialization.Serializable

/** 할인 분담 정책 예약 업데이트 재설정을 위한 입력 정보 */
@Serializable
public data class ReschedulePlatformDiscountSharePolicyBody(
  /** 반영할 업데이트 내용 */
  val update: UpdatePlatformDiscountSharePolicyBody,
  /** 업데이트 적용 시점 */
  val appliedAt: Instant,
)
