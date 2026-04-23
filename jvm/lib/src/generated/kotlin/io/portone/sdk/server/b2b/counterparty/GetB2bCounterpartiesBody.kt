package io.portone.sdk.server.b2b.counterparty

import io.portone.sdk.server.b2b.counterparty.B2bCounterpartyFilter
import io.portone.sdk.server.common.PageInput
import kotlinx.serialization.Serializable

/** 거래처 검색 요청 정보 */
@Serializable
internal data class GetB2bCounterpartiesBody(
  /** 페이지 정보 */
  val page: PageInput? = null,
  /** 검색 필터 */
  val filter: B2bCounterpartyFilter? = null,
)


