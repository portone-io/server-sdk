package io.portone.sdk.server.errors

public sealed interface CreatePaymentSessionException : PaymentSessionException {
  public override val message: String?
}
