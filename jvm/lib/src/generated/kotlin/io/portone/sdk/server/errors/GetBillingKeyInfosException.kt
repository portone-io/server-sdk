package io.portone.sdk.server.errors

public sealed interface GetBillingKeyInfosException : PaymentBillingKeyException {
  public override val message: String?
}
