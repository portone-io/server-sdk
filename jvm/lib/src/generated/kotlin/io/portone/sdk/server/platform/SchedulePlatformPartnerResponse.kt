package io.portone.sdk.server.platform

import io.portone.sdk.server.platform.PlatformPartner
import kotlinx.serialization.Serializable

/** 파트너 업데이트 예약 성공 응답 */
@Serializable
public data class SchedulePlatformPartnerResponse(
  /** 예약된 파트너 정보 */
  val scheduledPartner: PlatformPartner,
)
