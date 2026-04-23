package io.portone.sdk.server.errors

public sealed interface ConfirmPaymentwallDeliveryException : PgSpecificException {
  public override val message: String?
}
