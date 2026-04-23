package io.portone.sdk.server.errors

public sealed interface UpdateB2bCounterpartyException : B2bCounterpartyException {
  public override val message: String?
}
