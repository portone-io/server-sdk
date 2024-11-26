package io.portone.sdk.server.errors

public sealed interface PlatformPayoutException : PlatformException {
  public override val message: String?
}
