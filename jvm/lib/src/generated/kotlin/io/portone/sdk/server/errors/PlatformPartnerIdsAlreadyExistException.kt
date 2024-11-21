package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformPartnerIdsAlreadyExistError
import java.lang.Exception
import kotlin.Array
import kotlin.String


public class PlatformPartnerIdsAlreadyExistException internal constructor(
  cause: PlatformPartnerIdsAlreadyExistError
) : PortOneException(cause.message), CreatePlatformPartnersException {
  public val ids: List<String> = cause.ids
  public val graphqlIds: List<String> = cause.graphqlIds
}
