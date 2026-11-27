package io.portone.sdk.server.errors

public sealed interface ClosePaymentSessionException : PaymentSessionException {
  public override val message: String?
}
