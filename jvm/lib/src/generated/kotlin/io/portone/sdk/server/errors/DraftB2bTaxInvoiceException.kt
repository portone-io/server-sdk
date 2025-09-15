package io.portone.sdk.server.errors

public sealed interface DraftB2bTaxInvoiceException : B2bTaxInvoiceException {
  public override val message: String?
}
