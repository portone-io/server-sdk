package io.portone.sdk.server.errors

public sealed interface B2BBusinessException : B2BException {
  public override val message: String?
}
