package io.portone.sdk.server.errors

public sealed interface AuthException : RestException {
  public override val message: String?
}