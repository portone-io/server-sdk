package io.portone.sdk.server.errors

public sealed interface RecoverPlatformContractException : PlatformPolicyException {
  public override val message: String?
}
