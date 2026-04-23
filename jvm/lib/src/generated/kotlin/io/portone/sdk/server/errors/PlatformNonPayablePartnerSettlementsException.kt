package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformNonPayablePartnerSettlementsError
import java.lang.Exception
import kotlin.Array
import kotlin.String


/** 지급할 수 없는 정산건이 포함된 경우 */
public class PlatformNonPayablePartnerSettlementsException internal constructor(
  cause: PlatformNonPayablePartnerSettlementsError
) : PortOneException(cause.message), CompletePlatformPayoutByPartnerSettlementIdsException {
  public val ids: List<String> = cause.ids
  public val graphqlIds: List<String> = cause.graphqlIds
}
