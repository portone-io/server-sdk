package io.portone.sdk.server.platform.payout

import kotlin.Array
import kotlin.String
import kotlinx.serialization.Serializable

@Serializable
internal data class CompletePlatformPayoutByPartnerSettlementIdsBody(
  val bulkPayoutId: String,
  val name: String? = null,
  val partnerSettlementIds: List<String>,
  /**
   * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
   * (yyyy-MM-dd)
   */
  val completedAt: String? = null,
  /**
   * Query Parameter의 test에 값이 제공된 경우 Query Parameter의 test를 사용하고 해당 값은 무시됩니다.
   * Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
   */
  val isForTest: Boolean? = null,
)


