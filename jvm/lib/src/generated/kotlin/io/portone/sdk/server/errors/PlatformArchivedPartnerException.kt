package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformArchivedPartnerError
import java.lang.Exception


/** 보관된 파트너를 업데이트하려고 하는 경우 */
public class PlatformArchivedPartnerException internal constructor(
  cause: PlatformArchivedPartnerError
) : PortOneException(cause.message), SchedulePartnerException, UpdatePlatformPartnerException {
}
