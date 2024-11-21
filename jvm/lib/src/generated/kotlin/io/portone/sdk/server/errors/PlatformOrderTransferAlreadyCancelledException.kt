package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformOrderTransferAlreadyCancelledError
import java.lang.Exception


public class PlatformOrderTransferAlreadyCancelledException internal constructor(
  cause: PlatformOrderTransferAlreadyCancelledError
) : PortOneException(cause.message), CreatePlatformOrderCancelTransferException {
}
