package io.portone.sdk.server.errors

public sealed interface ConfirmBillingKeyException : PaymentBillingKeyException {
  public override val message: String?
}
