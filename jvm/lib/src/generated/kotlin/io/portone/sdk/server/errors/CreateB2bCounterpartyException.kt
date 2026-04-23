package io.portone.sdk.server.errors

public sealed interface CreateB2bCounterpartyException : B2bCounterpartyException {
  public override val message: String?
}
