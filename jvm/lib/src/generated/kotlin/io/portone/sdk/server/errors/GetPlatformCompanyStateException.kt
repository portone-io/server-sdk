package io.portone.sdk.server.errors

public sealed interface GetPlatformCompanyStateException : PlatformCompanyException {
  public override val message: String?
}
