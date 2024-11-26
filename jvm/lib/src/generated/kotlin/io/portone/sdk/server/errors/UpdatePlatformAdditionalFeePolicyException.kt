package io.portone.sdk.server.errors

public sealed interface UpdatePlatformAdditionalFeePolicyException : PlatformPolicyException {
  public override val message: String?
}
