package io.portone.sdk.server.errors

public sealed interface GetPlatformContractsException : PlatformPolicyException {
  public override val message: String?
}
