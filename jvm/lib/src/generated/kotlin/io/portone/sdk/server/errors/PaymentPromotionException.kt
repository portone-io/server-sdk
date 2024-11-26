package io.portone.sdk.server.errors

public sealed interface PaymentPromotionException : PaymentException {
  public override val message: String?
}
