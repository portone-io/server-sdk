package io.portone.sdk.server.errors

public sealed interface GetPlatformTransferException : PlatformTransferException {
  public override val message: String?
}
