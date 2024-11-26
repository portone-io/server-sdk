package io.portone.sdk.server.errors

public sealed interface GetPaymentException : PaymentException {
  public override val message: String?
}
