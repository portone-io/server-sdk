package io.portone.sdk.server.errors

public sealed interface CreateB2bFileUploadUrlException : B2bTaxInvoiceException {
  public override val message: String?
}
