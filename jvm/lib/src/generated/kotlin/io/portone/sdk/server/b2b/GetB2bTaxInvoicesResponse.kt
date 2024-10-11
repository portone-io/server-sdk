package io.portone.sdk.server.b2b

import io.portone.sdk.server.b2b.B2bTaxInvoiceSummary
import io.portone.sdk.server.common.PageInfo
import kotlinx.serialization.Serializable

/** 세금계산서 다건 조회 성공 응답 */
@Serializable
public data class GetB2bTaxInvoicesResponse(
  /** 조회된 세금계산서 목록 */
  val items: List<B2bTaxInvoiceSummary>,
  /** 조회된 페이지 정보 */
  val page: PageInfo,
)
