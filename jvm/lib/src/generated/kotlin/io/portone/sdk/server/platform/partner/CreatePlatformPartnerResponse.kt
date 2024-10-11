package io.portone.sdk.server.platform.partner

import io.portone.sdk.server.platform.PlatformPartner
import kotlinx.serialization.Serializable

/** 파트너 생성 성공 응답 */
@Serializable
public data class CreatePlatformPartnerResponse(
  /** 생성된 파트너 */
  val partner: PlatformPartner,
)
