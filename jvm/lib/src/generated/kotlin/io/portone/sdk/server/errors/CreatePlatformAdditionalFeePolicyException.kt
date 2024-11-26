package io.portone.sdk.server.errors

public sealed interface CreatePlatformAdditionalFeePolicyException : PlatformPolicyException {
  public override val message: String?
}
