package io.portone.sdk.server.errors

public sealed interface CapturePaymentException : PaymentException {
  public override val message: String?
}
