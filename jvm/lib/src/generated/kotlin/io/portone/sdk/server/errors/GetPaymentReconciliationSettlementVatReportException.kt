package io.portone.sdk.server.errors

public sealed interface GetPaymentReconciliationSettlementVatReportException : ReconciliationException {
  public override val message: String?
}
