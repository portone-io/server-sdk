package io.portone.sdk.server.errors

public sealed interface GetB2bCounterpartyException : B2bCounterpartyException {
  public override val message: String?
}
