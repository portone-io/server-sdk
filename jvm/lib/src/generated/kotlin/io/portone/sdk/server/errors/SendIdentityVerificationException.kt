package io.portone.sdk.server.errors

public sealed interface SendIdentityVerificationException : IdentityVerificationException {
  public override val message: String?
}
