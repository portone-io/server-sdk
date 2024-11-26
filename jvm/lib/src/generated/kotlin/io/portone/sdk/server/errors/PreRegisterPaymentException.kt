package io.portone.sdk.server.errors

public sealed interface PreRegisterPaymentException : PaymentException {
  public override val message: String?
}
