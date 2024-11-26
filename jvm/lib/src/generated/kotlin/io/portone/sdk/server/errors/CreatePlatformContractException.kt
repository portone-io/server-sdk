package io.portone.sdk.server.errors

public sealed interface CreatePlatformContractException : PlatformPolicyException {
  public override val message: String?
}
