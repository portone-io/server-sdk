package io.portone.sdk.server.errors

public sealed interface GetPaymentReconciliationTransactionVatReportException : ReconciliationException {
  public override val message: String?
}
