package io.portone.sdk.server.platform

import io.portone.sdk.server.platform.UpdatePlatformPartnerBody
import kotlinx.datetime.Instant
import kotlinx.serialization.Serializable

/** 파트너 예약 업데이트 재설정을 위한 입력 정보 */
@Serializable
public data class ReschedulePlatformPartnerBody(
  /** 반영할 업데이트 내용 */
  val update: UpdatePlatformPartnerBody,
  /** 업데이트 적용 시점 */
  val appliedAt: Instant,
)
