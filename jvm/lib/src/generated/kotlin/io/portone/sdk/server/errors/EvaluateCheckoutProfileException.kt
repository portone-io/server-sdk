package io.portone.sdk.server.errors

public sealed interface EvaluateCheckoutProfileException : CheckoutProfileException {
  public override val message: String?
}
