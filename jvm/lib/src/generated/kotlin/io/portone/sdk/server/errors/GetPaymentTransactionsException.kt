package io.portone.sdk.server.errors

public sealed interface GetPaymentTransactionsException : PaymentException {
  public override val message: String?
}
