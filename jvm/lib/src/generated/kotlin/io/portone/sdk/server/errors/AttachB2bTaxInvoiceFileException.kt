package io.portone.sdk.server.errors

public sealed interface AttachB2bTaxInvoiceFileException : B2bTaxInvoiceException {
  public override val message: String?
}
