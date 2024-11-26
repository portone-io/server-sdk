package io.portone.sdk.server.errors

public sealed interface GetIdentityVerificationException : IdentityVerificationException {
  public override val message: String?
}
