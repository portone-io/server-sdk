package io.portone.sdk.server.platform.partnersettlement

import io.portone.sdk.server.common.PageInfo
import io.portone.sdk.server.platform.partnersettlement.PlatformPartnerSettlement
import io.portone.sdk.server.platform.partnersettlement.PlatformPartnerSettlementStatusStats
import kotlinx.serialization.Serializable

/** 정산내역 다건 조회 성공 응답 정보 */
@Serializable
public data class GetPlatformPartnerSettlementsResponse(
  /** 조회된 정산내역 리스트 */
  val items: List<PlatformPartnerSettlement>,
  /** 조회된 페이지 정보 */
  val page: PageInfo,
  /** 정산내역 상태 별 갯수 */
  val counts: PlatformPartnerSettlementStatusStats,
)


