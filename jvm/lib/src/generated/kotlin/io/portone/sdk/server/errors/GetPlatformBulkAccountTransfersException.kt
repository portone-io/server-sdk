package io.portone.sdk.server.errors

public sealed interface GetPlatformBulkAccountTransfersException : PlatformBulkAccountTransferException {
  public override val message: String?
}
