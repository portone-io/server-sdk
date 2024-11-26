package io.portone.sdk.server.errors

public sealed interface ModifyEscrowLogisticsException : PaymentException {
  public override val message: String?
}
