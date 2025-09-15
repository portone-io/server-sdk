package io.portone.sdk.server.errors

public sealed interface ConfirmPaymentException : PaymentException {
  public override val message: String?
}
