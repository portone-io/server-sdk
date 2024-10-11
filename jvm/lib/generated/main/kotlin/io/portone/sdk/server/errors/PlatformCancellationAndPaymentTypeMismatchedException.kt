package io.portone.sdk.server.errors

import io.portone.sdk.server.platform.transfer.PlatformCancellationAndPaymentTypeMismatchedError
import java.lang.Exception


public class PlatformCancellationAndPaymentTypeMismatchedException(
  cause: PlatformCancellationAndPaymentTypeMismatchedError
) : Exception(cause.message) {
}
