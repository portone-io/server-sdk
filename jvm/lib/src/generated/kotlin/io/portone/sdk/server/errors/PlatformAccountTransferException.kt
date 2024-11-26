package io.portone.sdk.server.errors

public sealed interface PlatformAccountTransferException : PlatformException {
  public override val message: String?
}
