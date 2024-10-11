package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformDiscountSharePolicyScheduleAlreadyExistsError
import java.lang.Exception


public class PlatformDiscountSharePolicyScheduleAlreadyExistsException(
  cause: PlatformDiscountSharePolicyScheduleAlreadyExistsError
) : Exception(cause.message) {
}
