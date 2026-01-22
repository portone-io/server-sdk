package io.portone.sdk.server.reconciliation

import io.portone.sdk.server.reconciliation.PaymentReconciliationVatReportItem
import io.portone.sdk.server.reconciliation.PaymentReconciliationVatReportSummary
import io.portone.sdk.server.reconciliation.ReconciliationPgSpecifier
import kotlinx.serialization.Serializable

@Serializable
public data class GetPaymentReconciliationSettlementVatReportResponse(
  /** 부가세 내역 항목 리스트 */
  val items: List<PaymentReconciliationVatReportItem>? = null,
  /** 부가세 내역 요약 */
  val summary: PaymentReconciliationVatReportSummary,
  /** PG사 식별자 리스트 */
  val pgSpecifiers: List<ReconciliationPgSpecifier>? = null,
)


