package io.portone.sdk.server.errors

public sealed interface PlatformCompanyException : PlatformException {
  public override val message: String?
}
