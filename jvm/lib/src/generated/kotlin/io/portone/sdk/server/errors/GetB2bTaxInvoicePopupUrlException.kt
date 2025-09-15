package io.portone.sdk.server.errors

public sealed interface GetB2bTaxInvoicePopupUrlException : B2bTaxInvoiceException {
  public override val message: String?
}
