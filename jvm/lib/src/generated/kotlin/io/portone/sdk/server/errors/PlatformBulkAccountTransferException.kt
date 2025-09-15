package io.portone.sdk.server.errors

public sealed interface PlatformBulkAccountTransferException : PlatformException {
  public override val message: String?
}
