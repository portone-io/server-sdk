package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformDiscountSharePolicyScheduleAlreadyExistsError
import java.lang.Exception


public class PlatformDiscountSharePolicyScheduleAlreadyExistsException internal constructor(
  cause: PlatformDiscountSharePolicyScheduleAlreadyExistsError
) : PortOneException(cause.message), ScheduleDiscountSharePolicyException {
}
