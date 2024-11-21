package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformTransferNotFoundError
import java.lang.Exception


public class PlatformTransferNotFoundException internal constructor(
  cause: PlatformTransferNotFoundError
) : PortOneException(cause.message), CreatePlatformOrderCancelTransferException, DeletePlatformTransferException, GetPlatformTransferException {
}
