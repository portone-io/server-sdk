package io.portone.sdk.server.errors

public sealed interface GetB2bTaxInvoicesException : B2bTaxInvoiceException {
  public override val message: String?
}
