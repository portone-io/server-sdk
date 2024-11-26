package io.portone.sdk.server.errors

public sealed interface PayInstantlyException : PaymentException {
  public override val message: String?
}
