package io.portone.sdk.server.errors

public sealed interface GetPgCardPromotionsException : PaymentAdditionalFeatureException {
  public override val message: String?
}
