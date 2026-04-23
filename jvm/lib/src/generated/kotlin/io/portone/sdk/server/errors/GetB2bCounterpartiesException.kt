package io.portone.sdk.server.errors

public sealed interface GetB2bCounterpartiesException : B2bCounterpartyException {
  public override val message: String?
}
