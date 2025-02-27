package io.portone.sdk.server.errors

public sealed interface ConnectPartnerMemberCompanyException : PlatformPartnerException {
  public override val message: String?
}
