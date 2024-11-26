package io.portone.sdk.server.errors

public sealed interface CancelPaymentException : PaymentException {
  public override val message: String?
}
