package io.portone.sdk.server.errors

public sealed interface UpdatePlatformException : PlatformException {
  public override val message: String?
}
