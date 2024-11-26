package io.portone.sdk.server.errors

public sealed interface DownloadPlatformTransferSheetException : PlatformTransferException {
  public override val message: String?
}
