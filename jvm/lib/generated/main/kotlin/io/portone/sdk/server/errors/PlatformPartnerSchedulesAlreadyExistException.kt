package io.portone.sdk.server.errors

import io.portone.sdk.server.platform.PlatformPartnerSchedulesAlreadyExistError
import java.lang.Exception
import kotlin.Array
import kotlin.String


public class PlatformPartnerSchedulesAlreadyExistException(
  cause: PlatformPartnerSchedulesAlreadyExistError
) : Exception(cause.message) {
  public val ids: Array<String> = cause.ids,
  public val graphqlIds: Array<String> = cause.graphqlIds,
}
