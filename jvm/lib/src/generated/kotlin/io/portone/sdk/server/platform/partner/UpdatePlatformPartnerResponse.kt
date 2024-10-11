package io.portone.sdk.server.platform.partner

import io.portone.sdk.server.platform.PlatformPartner
import kotlinx.serialization.Serializable

/** 파트너 업데이트 성공 응답 */
@Serializable
public data class UpdatePlatformPartnerResponse(
  /** 업데이트된 파트너 */
  val partner: PlatformPartner,
)
