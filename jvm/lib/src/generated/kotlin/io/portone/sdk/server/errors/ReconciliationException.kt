package io.portone.sdk.server.errors

public sealed interface ReconciliationException : RestException {
  public override val message: String?
}
