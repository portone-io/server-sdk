package io.portone.sdk.server.platform

import io.portone.sdk.server.platform.PlatformPartner
import kotlinx.serialization.Serializable

/** 파트너 예약 업데이트 재설정 성공 응답 */
@Serializable
public data class ReschedulePlatformPartnerResponse(
  /** 예약된 파트너 정보 */
  val scheduledPartner: PlatformPartner,
)
