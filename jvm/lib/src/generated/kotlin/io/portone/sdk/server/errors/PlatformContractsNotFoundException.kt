package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformContractsNotFoundError
import java.lang.Exception
import kotlin.Array
import kotlin.String


public class PlatformContractsNotFoundException internal constructor(
  cause: PlatformContractsNotFoundError
) : PortOneException(cause.message), CreatePlatformPartnersException {
  public val ids: List<String> = cause.ids
  public val graphqlIds: List<String> = cause.graphqlIds
}
