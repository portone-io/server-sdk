package io.portone.sdk.server.errors

public sealed interface CancelPlatformAdditionalFeePolicyScheduleException : PlatformException {
  public override val message: String?
}
