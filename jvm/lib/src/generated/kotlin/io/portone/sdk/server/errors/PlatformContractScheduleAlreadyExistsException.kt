package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformContractScheduleAlreadyExistsError
import java.lang.Exception


public class PlatformContractScheduleAlreadyExistsException(
  cause: PlatformContractScheduleAlreadyExistsError
) : Exception(cause.message) {
}
