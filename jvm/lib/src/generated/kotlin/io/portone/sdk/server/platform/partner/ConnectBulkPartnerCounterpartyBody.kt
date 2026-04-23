package io.portone.sdk.server.platform.partner

import io.portone.sdk.server.platform.PlatformPartnerFilterInput
import kotlinx.serialization.Serializable

/**
 * 파트너 일괄 거래처 연동 요청 정보
 *
 * 파트너들을 일괄 거래처 연동합니다.
 */
@Serializable
internal data class ConnectBulkPartnerCounterpartyBody(
  /** 일괄 거래처 연동할 파트너 조건 필터 */
  val filter: PlatformPartnerFilterInput? = null,
)


