package io.portone.sdk.server.errors

public sealed interface ResendIdentityVerificationException : IdentityVerificationException {
  public override val message: String?
}
