package io.portone.sdk.server.platform.partner

import io.portone.sdk.server.platform.partner.PlatformBulkTask
import kotlinx.serialization.Serializable

/** 파트너 일괄 거래처 연동 해제 응답 */
@Serializable
public data class DisconnectBulkPartnerCounterpartyResponse(
  val bulkTask: PlatformBulkTask,
)


