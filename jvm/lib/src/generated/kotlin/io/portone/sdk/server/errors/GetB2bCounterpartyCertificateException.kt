package io.portone.sdk.server.errors

public sealed interface GetB2bCounterpartyCertificateException : B2bCounterpartyException {
  public override val message: String?
}
