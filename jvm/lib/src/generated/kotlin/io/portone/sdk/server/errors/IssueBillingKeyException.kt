package io.portone.sdk.server.errors

public sealed interface IssueBillingKeyException : PaymentBillingKeyException {
  public override val message: String?
}
