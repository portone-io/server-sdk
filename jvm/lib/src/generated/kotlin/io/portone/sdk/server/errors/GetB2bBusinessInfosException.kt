package io.portone.sdk.server.errors

public sealed interface GetB2bBusinessInfosException : PlatformCompanyException {
  public override val message: String?
}
