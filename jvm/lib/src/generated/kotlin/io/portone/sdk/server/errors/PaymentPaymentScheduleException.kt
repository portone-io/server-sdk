package io.portone.sdk.server.errors

public sealed interface PaymentPaymentScheduleException : PaymentException {
  public override val message: String?
}
