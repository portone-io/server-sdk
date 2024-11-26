package io.portone.sdk.server.errors

public sealed interface UpdatePlatformContractException : PlatformPolicyException {
  public override val message: String?
}
