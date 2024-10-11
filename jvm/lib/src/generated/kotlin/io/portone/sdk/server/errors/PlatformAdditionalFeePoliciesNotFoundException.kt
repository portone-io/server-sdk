package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformAdditionalFeePoliciesNotFoundError
import java.lang.Exception
import kotlin.Array
import kotlin.String


public class PlatformAdditionalFeePoliciesNotFoundException(
  cause: PlatformAdditionalFeePoliciesNotFoundError
) : Exception(cause.message) {
  public val ids: Array<String> = cause.ids
  public val graphqlIds: Array<String> = cause.graphqlIds
}
