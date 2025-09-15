package io.portone.sdk.server.errors

public sealed interface CancelB2bTaxInvoiceIssuanceException : B2bTaxInvoiceException {
  public override val message: String?
}
