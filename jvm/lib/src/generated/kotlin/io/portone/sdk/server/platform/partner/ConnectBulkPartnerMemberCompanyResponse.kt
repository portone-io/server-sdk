package io.portone.sdk.server.platform.partner

import io.portone.sdk.server.platform.partner.PlatformBulkTask
import kotlinx.serialization.Serializable

/** 파트너 일괄 국세청 연동 응답 */
@Serializable
public data class ConnectBulkPartnerMemberCompanyResponse(
  val bulkTask: PlatformBulkTask,
)


