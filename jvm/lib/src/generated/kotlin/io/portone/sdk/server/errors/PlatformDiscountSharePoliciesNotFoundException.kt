package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformDiscountSharePoliciesNotFoundError
import java.lang.Exception
import kotlin.Array
import kotlin.String


public class PlatformDiscountSharePoliciesNotFoundException(
  cause: PlatformDiscountSharePoliciesNotFoundError
) : Exception(cause.message) {
  public val ids: List<String> = cause.ids
  public val graphqlIds: List<String> = cause.graphqlIds
}
