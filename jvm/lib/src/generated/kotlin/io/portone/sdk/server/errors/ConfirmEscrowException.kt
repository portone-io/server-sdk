package io.portone.sdk.server.errors

public sealed interface ConfirmEscrowException : PaymentException {
  public override val message: String?
}
