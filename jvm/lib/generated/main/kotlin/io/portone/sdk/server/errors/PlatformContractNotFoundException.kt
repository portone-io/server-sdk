package io.portone.sdk.server.errors

import io.portone.sdk.server.platform.PlatformContractNotFoundError
import java.lang.Exception


public class PlatformContractNotFoundException(
  cause: PlatformContractNotFoundError
) : Exception(cause.message) {
}
