package io.portone.sdk.server.errors

public sealed interface GetPlatformPartnerFilterOptionsException : PlatformException {
  public override val message: String?
}
