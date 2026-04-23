package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformPartnerSettlementsNotFoundError
import java.lang.Exception
import kotlin.Array
import kotlin.String


/** 요청한 정산건 목록을 찾을 수 없는 경우 */
public class PlatformPartnerSettlementsNotFoundException internal constructor(
  cause: PlatformPartnerSettlementsNotFoundError
) : PortOneException(cause.message), CompletePlatformPayoutByPartnerSettlementIdsException, DeletePlatformPartnerSettlementsException {
  public val ids: List<String> = cause.ids
  public val graphqlIds: List<String> = cause.graphqlIds
}
