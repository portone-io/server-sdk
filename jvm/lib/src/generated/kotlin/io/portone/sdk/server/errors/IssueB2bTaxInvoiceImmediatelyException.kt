package io.portone.sdk.server.errors

public sealed interface IssueB2bTaxInvoiceImmediatelyException : B2bTaxInvoiceException {
  public override val message: String?
}
