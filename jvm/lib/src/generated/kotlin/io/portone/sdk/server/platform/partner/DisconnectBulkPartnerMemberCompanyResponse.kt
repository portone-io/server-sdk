package io.portone.sdk.server.platform.partner

import io.portone.sdk.server.platform.partner.PlatformBulkTask
import kotlinx.serialization.Serializable

/** 파트너 연동 사업자 일괄 연동 해제 요청 응답 */
@Serializable
public data class DisconnectBulkPartnerMemberCompanyResponse(
  val bulkTask: PlatformBulkTask,
)


