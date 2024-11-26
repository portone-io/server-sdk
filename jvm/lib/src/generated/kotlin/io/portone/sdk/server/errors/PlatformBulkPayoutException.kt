package io.portone.sdk.server.errors

public sealed interface PlatformBulkPayoutException : PlatformException {
  public override val message: String?
}
