package io.portone.sdk.server.platform.partner

import io.portone.sdk.server.platform.PlatformPartner
import kotlinx.serialization.Serializable

/** 파트너 연동 사업자 연동 요청 응답 */
@Serializable
public data class ConnectPartnerMemberCompanyResponse(
  val partner: PlatformPartner,
)


