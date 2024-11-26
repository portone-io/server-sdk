package io.portone.sdk.server.errors

public sealed interface GetPlatformBulkPayoutsException : PlatformBulkPayoutException {
  public override val message: String?
}
