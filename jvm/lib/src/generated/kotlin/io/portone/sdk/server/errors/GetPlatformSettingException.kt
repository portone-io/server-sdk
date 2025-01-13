package io.portone.sdk.server.errors

public sealed interface GetPlatformSettingException : PlatformException {
  public override val message: String?
}
