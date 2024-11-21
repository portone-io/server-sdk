package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformTransferNonDeletableStatusError
import java.lang.Exception


public class PlatformTransferNonDeletableStatusException internal constructor(
  cause: PlatformTransferNonDeletableStatusError
) : PortOneException(cause.message), DeletePlatformTransferException {
}
