package io.portone.sdk.server.errors

public sealed interface RequestB2bTaxInvoiceReverseIssuanceException : B2bTaxInvoiceException {
  public override val message: String?
}
