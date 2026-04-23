package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformTransferIdAlreadyUsedError
import java.lang.Exception


public class PlatformTransferIdAlreadyUsedException internal constructor(
  cause: PlatformTransferIdAlreadyUsedError
) : PortOneException(cause.message), CreatePlatformManualTransferException, CreatePlatformOrderCancelTransferException, CreatePlatformOrderTransferException {
}
