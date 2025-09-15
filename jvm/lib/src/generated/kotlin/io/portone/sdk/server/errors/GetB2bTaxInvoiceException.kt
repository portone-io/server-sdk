package io.portone.sdk.server.errors

public sealed interface GetB2bTaxInvoiceException : B2bTaxInvoiceException {
  public override val message: String?
}
