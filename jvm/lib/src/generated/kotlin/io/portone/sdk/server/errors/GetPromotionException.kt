package io.portone.sdk.server.errors

public sealed interface GetPromotionException : PaymentPromotionException {
  public override val message: String?
}
