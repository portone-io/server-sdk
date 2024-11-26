package io.portone.sdk.server.errors

public sealed interface GetCashReceiptException : PaymentCashReceiptException {
  public override val message: String?
}
