package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformAdditionalFeePolicyNotFoundError
import java.lang.Exception


public class PlatformAdditionalFeePolicyNotFoundException internal constructor(
  cause: PlatformAdditionalFeePolicyNotFoundError
) : PortOneException(cause.message), ArchivePlatformAdditionalFeePolicyException, CancelPlatformAdditionalFeePolicyScheduleException, GetPlatformAdditionalFeePolicyException, GetPlatformAdditionalFeePolicyScheduleException, RecoverPlatformAdditionalFeePolicyException, RescheduleAdditionalFeePolicyException, ScheduleAdditionalFeePolicyException, UpdatePlatformAdditionalFeePolicyException {
}
