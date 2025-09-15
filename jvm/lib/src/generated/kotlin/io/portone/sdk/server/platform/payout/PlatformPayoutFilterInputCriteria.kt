package io.portone.sdk.server.platform.payout

import io.portone.sdk.server.common.DateTimeRange
import kotlin.String
import kotlinx.serialization.Serializable

/** 검색 기준 입력 정보 */
@Serializable
public data class PlatformPayoutFilterInputCriteria(
  /** 생성 일시 범위 */
  val timestampRange: DateTimeRange? = null,
  /** 상태 업데이트 일시 범위 */
  val statusUpdatedTimestampRange: DateTimeRange? = null,
  /** 지급 예정 일시 범위 */
  val scheduledTimestampRange: DateTimeRange? = null,
  /** 정산 내역서 발송 일시 범위 */
  val settlementStatementIssuedTimestampRange: DateTimeRange? = null,
  /** 지급 아이디 */
  val payoutId: String? = null,
  /** 일괄 지급 아이디 */
  val bulkPayoutId: String? = null,
  /** 세금계산서 아이디 */
  val taxInvoiceId: String? = null,
  /** 정산 내역서 아이디 */
  val settlementStatementId: String? = null,
)


