package io.portone.sdk.server.errors

public sealed interface CreatePlatformManualTransferException : PlatformTransferException {
  public override val message: String?
}
