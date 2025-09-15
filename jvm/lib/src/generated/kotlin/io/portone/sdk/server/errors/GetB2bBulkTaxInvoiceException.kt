package io.portone.sdk.server.errors

public sealed interface GetB2bBulkTaxInvoiceException : B2bTaxInvoiceException {
  public override val message: String?
}
