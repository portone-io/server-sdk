package io.portone.sdk.server.errors

public sealed interface UpdatePlatformSettingException : PlatformException {
  public override val message: String?
}
