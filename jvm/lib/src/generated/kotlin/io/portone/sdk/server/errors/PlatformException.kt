package io.portone.sdk.server.errors

public sealed interface PlatformException : RestException {
  public override val message: String?
}
