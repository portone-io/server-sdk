package io.portone.sdk.server.errors

public sealed interface PgSpecificException : RestException {
  public override val message: String?
}
