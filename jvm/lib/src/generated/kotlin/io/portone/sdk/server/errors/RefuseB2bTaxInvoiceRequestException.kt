package io.portone.sdk.server.errors

public sealed interface RefuseB2bTaxInvoiceRequestException : B2bTaxInvoiceException {
  public override val message: String?
}
