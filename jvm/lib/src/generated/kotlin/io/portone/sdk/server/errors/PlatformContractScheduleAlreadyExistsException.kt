package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformContractScheduleAlreadyExistsError
import java.lang.Exception


public class PlatformContractScheduleAlreadyExistsException internal constructor(
  cause: PlatformContractScheduleAlreadyExistsError
) : PortOneException(cause.message), ScheduleContractException {
}
