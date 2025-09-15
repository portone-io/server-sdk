package io.portone.sdk.server.errors

public sealed interface GetB2bTaxInvoiceAttachmentsException : B2bTaxInvoiceException {
  public override val message: String?
}
