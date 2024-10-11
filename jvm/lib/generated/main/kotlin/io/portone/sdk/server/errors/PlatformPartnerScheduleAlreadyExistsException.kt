package io.portone.sdk.server.errors

import io.portone.sdk.server.platform.PlatformPartnerScheduleAlreadyExistsError
import java.lang.Exception


public class PlatformPartnerScheduleAlreadyExistsException(
  cause: PlatformPartnerScheduleAlreadyExistsError
) : Exception(cause.message) {
}
