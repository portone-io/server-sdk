package io.portone.sdk.server.errors

public sealed interface GetKakaopayPaymentOrderException : PgSpecificException {
  public override val message: String?
}
