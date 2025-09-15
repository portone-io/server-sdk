package io.portone.sdk.server.b2b.taxinvoice

import kotlinx.serialization.Serializable

/** 세금계산서 상태별 집계 정보 */
@Serializable
public data class B2bBulkTaxInvoiceStat(
  val count: Int,
  val amountSum: Long,
)


