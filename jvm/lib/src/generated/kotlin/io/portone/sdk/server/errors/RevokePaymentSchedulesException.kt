package io.portone.sdk.server.errors

public sealed interface RevokePaymentSchedulesException : PaymentPaymentScheduleException {
  public override val message: String?
}
