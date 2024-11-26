package io.portone.sdk.server.errors

public sealed interface GetPaymentScheduleException : PaymentPaymentScheduleException {
  public override val message: String?
}
