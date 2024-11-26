package io.portone.sdk.server.errors

public sealed interface GetPlatformContractScheduleException : PlatformException {
  public override val message: String?
}
