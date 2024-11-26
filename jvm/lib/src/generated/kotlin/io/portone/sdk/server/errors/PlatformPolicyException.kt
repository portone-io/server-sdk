package io.portone.sdk.server.errors

public sealed interface PlatformPolicyException : PlatformException {
  public override val message: String?
}
