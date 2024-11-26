package io.portone.sdk.server.errors

public sealed interface PlatformAccountException : PlatformException {
  public override val message: String?
}
