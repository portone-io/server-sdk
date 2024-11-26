package io.portone.sdk.server.errors

public sealed interface ConfirmIdentityVerificationException : IdentityVerificationException {
  public override val message: String?
}
