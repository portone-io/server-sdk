package io.portone.sdk.server.errors

public sealed interface UpdateB2bTaxInvoiceDraftException : B2bTaxInvoiceException {
  public override val message: String?
}
