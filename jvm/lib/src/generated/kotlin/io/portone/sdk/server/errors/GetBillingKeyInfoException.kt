package io.portone.sdk.server.errors

public sealed interface GetBillingKeyInfoException : PaymentBillingKeyException {
  public override val message: String?
}
