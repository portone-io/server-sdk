package io.portone.sdk.server.errors

public sealed interface B2bCounterpartyException : B2bException {
  public override val message: String?
}
