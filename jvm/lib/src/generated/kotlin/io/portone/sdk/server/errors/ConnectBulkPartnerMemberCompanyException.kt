package io.portone.sdk.server.errors

public sealed interface ConnectBulkPartnerMemberCompanyException : PlatformPartnerException {
  public override val message: String?
}
