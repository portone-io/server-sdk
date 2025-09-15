package io.portone.sdk.server.errors

public sealed interface requestB2bTaxInvoiceException : B2bTaxInvoiceException {
  public override val message: String?
}
