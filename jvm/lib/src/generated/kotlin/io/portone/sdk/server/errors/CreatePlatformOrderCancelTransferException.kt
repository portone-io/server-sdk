package io.portone.sdk.server.errors

public sealed interface CreatePlatformOrderCancelTransferException : PlatformTransferException {
  public override val message: String?
}
