package io.portone.sdk.server.reconciliation

import io.portone.sdk.server.common.DateRange
import io.portone.sdk.server.reconciliation.PaymentReconciliationTransactionSummaryFilterInput
import kotlinx.serialization.Serializable

@Serializable
internal data class GetPaymentReconciliationTransactionVatReportBody(
  /** 거래일 범위 */
  val dateRange: DateRange,
  val filter: PaymentReconciliationTransactionSummaryFilterInput? = null,
)


