package io.portone.sdk.server.errors

public sealed interface CancelCashReceiptException : PaymentCashReceiptException {
  public override val message: String?
}
