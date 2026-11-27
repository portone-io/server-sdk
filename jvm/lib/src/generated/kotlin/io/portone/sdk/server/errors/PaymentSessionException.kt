package io.portone.sdk.server.errors

public sealed interface PaymentSessionException : RestException {
  public override val message: String?
}
