package io.portone.sdk.server.errors

public sealed interface DownloadB2bTaxInvoicesSheetException : B2bTaxInvoiceException {
  public override val message: String?
}
