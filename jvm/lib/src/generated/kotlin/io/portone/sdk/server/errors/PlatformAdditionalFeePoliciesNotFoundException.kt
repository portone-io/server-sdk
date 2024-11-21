package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformAdditionalFeePoliciesNotFoundError
import java.lang.Exception
import kotlin.Array
import kotlin.String


public class PlatformAdditionalFeePoliciesNotFoundException internal constructor(
  cause: PlatformAdditionalFeePoliciesNotFoundError
) : PortOneException(cause.message), CreatePlatformOrderTransferException {
  public val ids: List<String> = cause.ids
  public val graphqlIds: List<String> = cause.graphqlIds
}
