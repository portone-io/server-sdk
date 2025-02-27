package io.portone.sdk.server.errors

public sealed interface GetCashReceiptsException : PaymentCashReceiptException {
  public override val message: String?
}
