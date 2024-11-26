package io.portone.sdk.server.errors

public sealed interface RefreshTokenException : AuthException {
  public override val message: String?
}
