package io.portone.sdk.server.errors

public sealed interface ConfirmBillingKeyIssueAndPayException : PaymentBillingKeyException {
  public override val message: String?
}
