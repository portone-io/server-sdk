package io.portone.sdk.server.errors

public sealed interface RescheduleAdditionalFeePolicyException : PlatformException {
  public override val message: String?
}
