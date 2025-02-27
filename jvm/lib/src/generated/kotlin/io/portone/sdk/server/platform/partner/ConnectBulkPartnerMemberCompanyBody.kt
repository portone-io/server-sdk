package io.portone.sdk.server.platform.partner

import io.portone.sdk.server.platform.PlatformPartnerFilterInput
import kotlinx.serialization.Serializable

/**
 * 파트너 연동 사업자 일괄 연동 요청 정보
 *
 * 파트너들을 연동 사업자로 일괄 연동합니다.
 */
@Serializable
internal data class ConnectBulkPartnerMemberCompanyBody(
  /** 연동 사업자로 일괄 연동할 파트너 조건 필터 */
  val filter: PlatformPartnerFilterInput? = null,
)


