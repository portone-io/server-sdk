package io.portone.sdk.server.errors

public sealed interface ApplyEscrowLogisticsException : PaymentException {
  public override val message: String?
}
