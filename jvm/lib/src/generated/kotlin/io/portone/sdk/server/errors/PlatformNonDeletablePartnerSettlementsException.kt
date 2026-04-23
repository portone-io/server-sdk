package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformNonDeletablePartnerSettlementsError
import java.lang.Exception
import kotlin.Array
import kotlin.String


/** 삭제할 수 없는 정산건이 포함된 경우 */
public class PlatformNonDeletablePartnerSettlementsException internal constructor(
  cause: PlatformNonDeletablePartnerSettlementsError
) : PortOneException(cause.message), DeletePlatformPartnerSettlementsException {
  public val ids: List<String> = cause.ids
  public val graphqlIds: List<String> = cause.graphqlIds
}
