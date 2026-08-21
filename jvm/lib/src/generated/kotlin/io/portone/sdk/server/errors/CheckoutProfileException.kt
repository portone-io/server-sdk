package io.portone.sdk.server.errors

public sealed interface CheckoutProfileException : RestException {
  public override val message: String?
}
