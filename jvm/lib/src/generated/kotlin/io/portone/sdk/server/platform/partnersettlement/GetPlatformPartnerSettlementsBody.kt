package io.portone.sdk.server.platform.partnersettlement

import io.portone.sdk.server.common.PageInput
import io.portone.sdk.server.platform.partnersettlement.PlatformPartnerSettlementFilterInput
import kotlinx.serialization.Serializable

/** 정산내역 다건 조회를 위한 입력 정보 */
@Serializable
internal data class GetPlatformPartnerSettlementsBody(
  /** 요청할 페이지 정보 */
  val page: PageInput? = null,
  /** 조회할 정산내역 조건 필터 */
  val filter: PlatformPartnerSettlementFilterInput,
  val isForTest: Boolean,
)
