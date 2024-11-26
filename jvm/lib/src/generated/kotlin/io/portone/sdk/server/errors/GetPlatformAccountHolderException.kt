package io.portone.sdk.server.errors

public sealed interface GetPlatformAccountHolderException : PlatformAccountException {
  public override val message: String?
}
