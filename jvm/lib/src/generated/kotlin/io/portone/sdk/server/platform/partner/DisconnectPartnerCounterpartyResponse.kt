package io.portone.sdk.server.platform.partner

import io.portone.sdk.server.platform.PlatformPartner
import kotlinx.serialization.Serializable

/** 파트너 거래처 연동 해제 응답 */
@Serializable
public data class DisconnectPartnerCounterpartyResponse(
  val partner: PlatformPartner,
)


