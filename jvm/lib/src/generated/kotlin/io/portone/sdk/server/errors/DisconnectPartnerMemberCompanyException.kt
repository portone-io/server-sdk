package io.portone.sdk.server.errors

public sealed interface DisconnectPartnerMemberCompanyException : PlatformPartnerException {
  public override val message: String?
}
