package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformCannotArchiveScheduledPartnerError
import java.lang.Exception


/** 예약된 업데이트가 있는 파트너를 보관하려고 하는 경우 */
public class PlatformCannotArchiveScheduledPartnerException internal constructor(
  cause: PlatformCannotArchiveScheduledPartnerError
) : PortOneException(cause.message), ArchivePlatformPartnerException {
}
