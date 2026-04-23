package io.portone.sdk.server.b2b.counterparty

import io.portone.sdk.server.b2b.counterparty.B2bCounterparty
import io.portone.sdk.server.common.PageInfo
import kotlinx.serialization.Serializable

/** 거래처 검색 성공 응답 */
@Serializable
public data class GetB2bCounterpartiesResponse(
  /** 페이지 정보 */
  val page: PageInfo,
  /** 거래처 목록 */
  val items: List<B2bCounterparty>,
)


