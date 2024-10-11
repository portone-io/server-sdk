package io.portone.sdk.server.errors

import io.portone.sdk.server.platform.transfer.PlatformTransferNonDeletableStatusError
import java.lang.Exception


public class PlatformTransferNonDeletableStatusException(
  cause: PlatformTransferNonDeletableStatusError
) : Exception(cause.message) {
}
