package io.portone.sdk.server.errors

public sealed interface ArchivePlatformContractException : PlatformPolicyException {
  public override val message: String?
}
