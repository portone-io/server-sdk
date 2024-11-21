package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformPaymentNotFoundError
import java.lang.Exception


public class PlatformPaymentNotFoundException internal constructor(
  cause: PlatformPaymentNotFoundError
) : PortOneException(cause.message), CreatePlatformOrderCancelTransferException, CreatePlatformOrderTransferException {
}
