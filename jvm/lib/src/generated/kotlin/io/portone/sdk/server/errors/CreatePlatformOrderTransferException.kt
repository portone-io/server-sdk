package io.portone.sdk.server.errors

public sealed interface CreatePlatformOrderTransferException : PlatformTransferException {
  public override val message: String?
}
