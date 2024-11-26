package io.portone.sdk.server.errors

public sealed interface GetPlatformAdditionalFeePolicyScheduleException : PlatformException {
  public override val message: String?
}
