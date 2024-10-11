package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformContractAlreadyExistsError
import java.lang.Exception


public class PlatformContractAlreadyExistsException(
  cause: PlatformContractAlreadyExistsError
) : Exception(cause.message) {
}
