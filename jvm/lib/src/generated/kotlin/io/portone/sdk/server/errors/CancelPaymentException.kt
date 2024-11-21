package io.portone.sdk.server.errors

public sealed interface CancelPaymentException {
  public val message: String?
}
