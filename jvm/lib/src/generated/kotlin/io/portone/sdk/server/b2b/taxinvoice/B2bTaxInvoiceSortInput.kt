package io.portone.sdk.server.b2b.taxinvoice

import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoiceSortBy
import io.portone.sdk.server.common.SortOrder
import kotlinx.serialization.Serializable

/** 세금계산서 다건 조회 시 정렬 조건 */
@Serializable
public data class B2bTaxInvoiceSortInput(
  /** 정렬 기준 */
  val by: B2bTaxInvoiceSortBy? = null,
  /** 정렬 방식 */
  val order: SortOrder? = null,
)


