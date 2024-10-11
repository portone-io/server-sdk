package io.portone.sdk.server.errors

import io.portone.sdk.server.platform.transfer.PlatformCancelOrderTransfersExistsError
import java.lang.Exception


public class PlatformCancelOrderTransfersExistsException(
  cause: PlatformCancelOrderTransfersExistsError
) : Exception(cause.message) {
}
