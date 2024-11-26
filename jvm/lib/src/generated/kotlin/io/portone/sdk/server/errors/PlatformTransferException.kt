package io.portone.sdk.server.errors

public sealed interface PlatformTransferException : PlatformException {
  public override val message: String?
}
