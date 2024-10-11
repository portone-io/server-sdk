package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformTransferNotFoundError
import java.lang.Exception


public class PlatformTransferNotFoundException(
  cause: PlatformTransferNotFoundError
) : Exception(cause.message) {
}
