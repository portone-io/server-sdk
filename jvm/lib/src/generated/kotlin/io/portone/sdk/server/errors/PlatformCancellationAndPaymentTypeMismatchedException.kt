package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformCancellationAndPaymentTypeMismatchedError
import java.lang.Exception


public class PlatformCancellationAndPaymentTypeMismatchedException internal constructor(
  cause: PlatformCancellationAndPaymentTypeMismatchedError
) : PortOneException(cause.message), CreatePlatformOrderCancelTransferException {
}
