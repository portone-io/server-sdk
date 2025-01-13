package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformMemberCompanyConnectedPartnersCannotBeScheduledError
import java.lang.Exception
import kotlin.Array
import kotlin.String


/** 연동 사업자로 연동된 파트너들을 예약 수정하려고 시도한 경우 */
public class PlatformMemberCompanyConnectedPartnersCannotBeScheduledException internal constructor(
  cause: PlatformMemberCompanyConnectedPartnersCannotBeScheduledError
) : PortOneException(cause.message), SchedulePlatformPartnersException {
  public val ids: List<String> = cause.ids
  public val graphqlIds: List<String> = cause.graphqlIds
}
