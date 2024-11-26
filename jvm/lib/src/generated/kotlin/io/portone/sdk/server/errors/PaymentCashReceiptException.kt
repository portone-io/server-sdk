package io.portone.sdk.server.errors

public sealed interface PaymentCashReceiptException : PaymentException {
  public override val message: String?
}
