package io.portone.sdk.server.errors

public sealed interface DeletePlatformTransferException : PlatformTransferException {
  public override val message: String?
}
