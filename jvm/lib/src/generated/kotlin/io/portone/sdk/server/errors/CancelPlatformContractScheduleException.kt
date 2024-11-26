package io.portone.sdk.server.errors

public sealed interface CancelPlatformContractScheduleException : PlatformException {
  public override val message: String?
}
