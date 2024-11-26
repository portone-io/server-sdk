package io.portone.sdk.server.errors

public sealed interface ResendWebhookException : PaymentException {
  public override val message: String?
}
