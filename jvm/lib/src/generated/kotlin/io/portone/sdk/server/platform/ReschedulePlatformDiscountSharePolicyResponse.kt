package io.portone.sdk.server.platform

import io.portone.sdk.server.platform.PlatformDiscountSharePolicy
import kotlinx.serialization.Serializable

/** 할인 분담 정책 예약 업데이트 재설정 성공 응답 */
@Serializable
public data class ReschedulePlatformDiscountSharePolicyResponse(
  /** 예약된 할인 분담 정보 */
  val scheduledDiscountSharePolicy: PlatformDiscountSharePolicy,
)
