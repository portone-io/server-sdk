package io.portone.sdk.server.errors

public sealed interface GetB2bTaxInvoicePrintUrlException : B2bTaxInvoiceException {
  public override val message: String?
}
