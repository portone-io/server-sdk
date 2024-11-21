package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformDiscountSharePolicyIdDuplicatedError
import java.lang.Exception
import kotlin.String


public class PlatformDiscountSharePolicyIdDuplicatedException internal constructor(
  cause: PlatformDiscountSharePolicyIdDuplicatedError
) : PortOneException(cause.message), CreatePlatformOrderCancelTransferException {
  public val id: String = cause.id
  public val graphqlId: String = cause.graphqlId
}
