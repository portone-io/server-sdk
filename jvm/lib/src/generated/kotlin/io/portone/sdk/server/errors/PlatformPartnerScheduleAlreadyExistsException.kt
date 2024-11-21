package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformPartnerScheduleAlreadyExistsError
import java.lang.Exception


public class PlatformPartnerScheduleAlreadyExistsException internal constructor(
  cause: PlatformPartnerScheduleAlreadyExistsError
) : PortOneException(cause.message), SchedulePartnerException {
}
