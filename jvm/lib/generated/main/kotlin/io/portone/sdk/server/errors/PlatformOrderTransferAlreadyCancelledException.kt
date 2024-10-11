package io.portone.sdk.server.errors

import io.portone.sdk.server.platform.transfer.PlatformOrderTransferAlreadyCancelledError
import java.lang.Exception


public class PlatformOrderTransferAlreadyCancelledException(
  cause: PlatformOrderTransferAlreadyCancelledError
) : Exception(cause.message) {
}
