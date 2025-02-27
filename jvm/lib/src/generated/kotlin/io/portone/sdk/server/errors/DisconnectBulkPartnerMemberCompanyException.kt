package io.portone.sdk.server.errors

public sealed interface DisconnectBulkPartnerMemberCompanyException : PlatformPartnerException {
  public override val message: String?
}
