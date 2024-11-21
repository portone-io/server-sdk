package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformAdditionalFeePolicyScheduleAlreadyExistsError
import java.lang.Exception


public class PlatformAdditionalFeePolicyScheduleAlreadyExistsException internal constructor(
  cause: PlatformAdditionalFeePolicyScheduleAlreadyExistsError
) : PortOneException(cause.message), ScheduleAdditionalFeePolicyException {
}
