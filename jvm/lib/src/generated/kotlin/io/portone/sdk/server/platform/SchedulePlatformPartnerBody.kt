package io.portone.sdk.server.platform

import io.portone.sdk.server.platform.UpdatePlatformPartnerBody
import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlinx.serialization.Serializable

/** 파트너 업데이트 예약을 위한 입력 정보 */
@Serializable
public data class SchedulePlatformPartnerBody(
  /** 반영할 업데이트 내용 */
  val update: UpdatePlatformPartnerBody,
  /** 업데이트 적용 시점 */
  val appliedAt: @Serializable(InstantSerializer::class) Instant,
)
