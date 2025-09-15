package io.portone.sdk.server.errors

public sealed interface B2bTaxInvoiceException : B2bException {
  public override val message: String?
}
