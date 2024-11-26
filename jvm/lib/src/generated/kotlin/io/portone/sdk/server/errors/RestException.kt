package io.portone.sdk.server.errors

public sealed interface RestException {
  public val message: String?
}
