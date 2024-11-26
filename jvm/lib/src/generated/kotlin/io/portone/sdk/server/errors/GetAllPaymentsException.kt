package io.portone.sdk.server.errors

public sealed interface GetAllPaymentsException : PaymentException {
  public override val message: String?
}
