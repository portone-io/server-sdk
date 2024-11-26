package io.portone.sdk.server.errors

public sealed interface RescheduleContractException : PlatformException {
  public override val message: String?
}
