package io.portone.sdk.server.errors

public sealed interface GetIdentityVerificationsException : IdentityVerificationException {
  public override val message: String?
}
