package io.portone.sdk.server.reconciliation

import io.portone.sdk.server.common.DateRange
import io.portone.sdk.server.reconciliation.PaymentReconciliationSettlementSummaryFilterInput
import kotlinx.serialization.Serializable

@Serializable
internal data class GetPaymentReconciliationSettlementVatReportBody(
  /** 정산일 범위 */
  val dateRange: DateRange,
  val filter: PaymentReconciliationSettlementSummaryFilterInput? = null,
)


