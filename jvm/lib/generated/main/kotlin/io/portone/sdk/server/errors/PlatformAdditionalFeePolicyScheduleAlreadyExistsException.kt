package io.portone.sdk.server.errors

import io.portone.sdk.server.platform.PlatformAdditionalFeePolicyScheduleAlreadyExistsError
import java.lang.Exception


public class PlatformAdditionalFeePolicyScheduleAlreadyExistsException(
  cause: PlatformAdditionalFeePolicyScheduleAlreadyExistsError
) : Exception(cause.message) {
}
