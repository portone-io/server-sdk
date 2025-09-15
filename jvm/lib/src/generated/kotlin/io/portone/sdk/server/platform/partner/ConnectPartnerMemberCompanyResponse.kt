package io.portone.sdk.server.platform.partner

import io.portone.sdk.server.platform.PlatformPartner
import kotlinx.serialization.Serializable

/** 파트너 국세청 연동 응답 */
@Serializable
public data class ConnectPartnerMemberCompanyResponse(
  val partner: PlatformPartner,
)


