package io.portone.sdk.server.errors

public sealed interface PaymentBillingKeyException : PaymentException {
  public override val message: String?
}
