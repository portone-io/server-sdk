package io.portone.sdk.server.errors

public sealed interface GetPaymentSessionException : PaymentSessionException {
  public override val message: String?
}
