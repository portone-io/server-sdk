package io.portone.sdk.server.errors

public sealed interface GetPlatformPayoutsException : PlatformPayoutException {
  public override val message: String?
}
