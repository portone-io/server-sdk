package io.portone.sdk.server.errors

public sealed interface CreatePaymentScheduleException : PaymentPaymentScheduleException {
  public override val message: String?
}
