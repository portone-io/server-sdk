package io.portone.sdk.server.errors

public sealed interface GetPaymentSchedulesException : PaymentPaymentScheduleException {
  public override val message: String?
}
