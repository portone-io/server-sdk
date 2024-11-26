package io.portone.sdk.server.errors

public sealed interface DeleteBillingKeyException : PaymentBillingKeyException {
  public override val message: String?
}
