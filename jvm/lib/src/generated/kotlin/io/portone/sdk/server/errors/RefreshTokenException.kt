package io.portone.sdk.server.errors

public sealed interface RefreshTokenException {
  public val message: String?
}
