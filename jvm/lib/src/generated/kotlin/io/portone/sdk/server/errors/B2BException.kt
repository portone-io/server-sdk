package io.portone.sdk.server.errors

public sealed interface B2BException : RestException {
  public override val message: String?
}
