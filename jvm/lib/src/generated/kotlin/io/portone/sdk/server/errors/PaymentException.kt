package io.portone.sdk.server.errors

public sealed interface PaymentException : RestException {
  public override val message: String?
}
