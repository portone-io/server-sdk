package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformArchivedPartnersCannotBeScheduledError
import java.lang.Exception


/** 보관된 파트너들을 예약 업데이트하려고 하는 경우 */
public class PlatformArchivedPartnersCannotBeScheduledException internal constructor(
  cause: PlatformArchivedPartnersCannotBeScheduledError
) : PortOneException(cause.message), SchedulePlatformPartnersException {
}
