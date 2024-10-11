package io.portone.sdk.server.errors

import io.portone.sdk.server.platform.transfer.PlatformOrderDetailMismatchedError
import java.lang.Exception


public class PlatformOrderDetailMismatchedException(
  cause: PlatformOrderDetailMismatchedError
) : Exception(cause.message) {
}
