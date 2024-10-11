package io.portone.sdk.server.errors

import io.portone.sdk.server.platform.transfer.PlatformDiscountSharePolicyIdDuplicatedError
import java.lang.Exception
import kotlin.String


public class PlatformDiscountSharePolicyIdDuplicatedException(
  cause: PlatformDiscountSharePolicyIdDuplicatedError
) : Exception(cause.message) {
  public val id: String = cause.id,
  public val graphqlId: String = cause.graphqlId,
}
