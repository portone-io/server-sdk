package io.portone.sdk.server.platform.partner

import io.portone.sdk.server.platform.PlatformPartner
import kotlinx.serialization.Serializable

/** 파트너 보관 성공 응답 */
@Serializable
public data class ArchivePlatformPartnerResponse(
  /** 보관된 파트너 */
  val partner: PlatformPartner,
)


