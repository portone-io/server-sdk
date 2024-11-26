package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformPartnerNotFoundError
import java.lang.Exception


public class PlatformPartnerNotFoundException internal constructor(
  cause: PlatformPartnerNotFoundError
) : PortOneException(cause.message), ArchivePlatformPartnerException, CancelPlatformPartnerScheduleException, CreatePlatformManualTransferException, CreatePlatformOrderTransferException, GetPlatformPartnerException, GetPlatformPartnerScheduleException, RecoverPlatformPartnerException, ReschedulePartnerException, SchedulePartnerException, UpdatePlatformPartnerException {
}
