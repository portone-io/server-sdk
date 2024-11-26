package io.portone.sdk.server.errors

public sealed interface GetPlatformException : PlatformException {
  public override val message: String?
}
