package io.portone.sdk.server.errors

public sealed interface PayWithBillingKeyException : PaymentException {
  public override val message: String?
}
