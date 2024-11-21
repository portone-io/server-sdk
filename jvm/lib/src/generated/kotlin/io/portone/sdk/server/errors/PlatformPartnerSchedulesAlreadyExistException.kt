package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformPartnerSchedulesAlreadyExistError
import java.lang.Exception
import kotlin.Array
import kotlin.String


public class PlatformPartnerSchedulesAlreadyExistException internal constructor(
  cause: PlatformPartnerSchedulesAlreadyExistError
) : PortOneException(cause.message), SchedulePlatformPartnersException {
  public val ids: List<String> = cause.ids
  public val graphqlIds: List<String> = cause.graphqlIds
}
