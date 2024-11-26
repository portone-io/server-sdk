package io.portone.sdk.server.errors

public sealed interface GetPlatformAccountTransfersException : PlatformAccountTransferException {
  public override val message: String?
}
