package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformCancelOrderTransfersExistsError
import java.lang.Exception


public class PlatformCancelOrderTransfersExistsException internal constructor(
  cause: PlatformCancelOrderTransfersExistsError
) : PortOneException(cause.message), DeletePlatformTransferException {
}
