package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformCancellationNotFoundError
import java.lang.Exception


public class PlatformCancellationNotFoundException internal constructor(
  cause: PlatformCancellationNotFoundError
) : PortOneException(cause.message), CreatePlatformOrderCancelTransferException {
}
