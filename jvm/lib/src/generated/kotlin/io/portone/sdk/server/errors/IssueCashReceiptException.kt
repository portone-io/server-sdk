package io.portone.sdk.server.errors

public sealed interface IssueCashReceiptException : PaymentCashReceiptException {
  public override val message: String?
}
