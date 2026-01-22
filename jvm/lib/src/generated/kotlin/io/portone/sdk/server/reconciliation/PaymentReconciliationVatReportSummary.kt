package io.portone.sdk.server.reconciliation

import kotlinx.serialization.Serializable

@Serializable
public data class PaymentReconciliationVatReportSummary(
  /** 총 공급가액 */
  val totalSupplyAmount: Long,
  /** 총 부가세 금액 */
  val totalVatAmount: Long,
  /** 총 면세 금액 */
  val totalTaxFreeAmount: Long,
  /** 총 금액 */
  val totalAmount: Long,
)


