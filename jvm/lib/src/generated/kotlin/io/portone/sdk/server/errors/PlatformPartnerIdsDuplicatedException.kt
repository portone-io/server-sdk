package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformPartnerIdsDuplicatedError
import java.lang.Exception
import kotlin.Array
import kotlin.String


public class PlatformPartnerIdsDuplicatedException(
  cause: PlatformPartnerIdsDuplicatedError
) : Exception(cause.message) {
  public val ids: List<String> = cause.ids
  public val graphqlIds: List<String> = cause.graphqlIds
}
