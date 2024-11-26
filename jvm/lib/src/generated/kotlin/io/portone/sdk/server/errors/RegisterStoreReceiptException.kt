package io.portone.sdk.server.errors

public sealed interface RegisterStoreReceiptException : PaymentException {
  public override val message: String?
}
