package io.portone.sdk.server.errors

public sealed interface IdentityVerificationException : RestException {
  public override val message: String?
}
