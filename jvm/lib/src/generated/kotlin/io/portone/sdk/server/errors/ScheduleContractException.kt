package io.portone.sdk.server.errors

public sealed interface ScheduleContractException : PlatformException {
  public override val message: String?
}
