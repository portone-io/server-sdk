package io.portone.sdk.server.errors

public sealed interface GetB2bTaxInvoicePdfDownloadUrlException : B2bTaxInvoiceException {
  public override val message: String?
}
