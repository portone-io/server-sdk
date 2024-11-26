package io.portone.sdk.server.errors

public sealed interface LoginViaApiSecretException : AuthException {
  public override val message: String?
}
