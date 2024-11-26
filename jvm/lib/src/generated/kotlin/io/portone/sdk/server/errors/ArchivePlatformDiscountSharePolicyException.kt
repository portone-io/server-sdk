package io.portone.sdk.server.errors

public sealed interface ArchivePlatformDiscountSharePolicyException : PlatformPolicyException {
  public override val message: String?
}
