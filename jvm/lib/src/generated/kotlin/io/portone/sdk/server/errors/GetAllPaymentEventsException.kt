package io.portone.sdk.server.errors

public sealed interface GetAllPaymentEventsException : PaymentException {
  public override val message: String?
}
