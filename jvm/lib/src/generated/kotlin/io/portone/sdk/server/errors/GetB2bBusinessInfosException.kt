package io.portone.sdk.server.errors

public sealed interface GetB2bBusinessInfosException : B2BBusinessException {
  public override val message: String?
}
