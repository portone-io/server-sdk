package io.portone.sdk.server.errors

public sealed interface GetPlatformContractException : PlatformPolicyException {
  public override val message: String?
}
