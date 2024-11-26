package io.portone.sdk.server.errors

public sealed interface GetPlatformTransferSummariesException : PlatformTransferException {
  public override val message: String?
}
