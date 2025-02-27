package io.portone.sdk.server.platform.partner

import io.portone.sdk.server.platform.PlatformPartner
import kotlinx.serialization.Serializable

/** 연동 사업자 연동 해제 요청 응답 */
@Serializable
public data class DisconnectPartnerMemberCompanyResponse(
  val partner: PlatformPartner,
)


