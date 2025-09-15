package io.portone.sdk.server.errors

public sealed interface B2bException : RestException {
  public override val message: String?
}
