package io.portone.sdk.server.errors

public sealed interface CloseVirtualAccountException : PaymentException {
  public override val message: String?
}
