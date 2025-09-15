package io.portone.sdk.server.platform.accounttransfer

import io.portone.sdk.server.common.DateTimeRange
import io.portone.sdk.server.platform.accounttransfer.PlatformAccountTransferStatus
import io.portone.sdk.server.platform.accounttransfer.PlatformAccountTransferType
import kotlin.Array
import kotlin.String
import kotlinx.serialization.Serializable

@Serializable
public data class PlatformAccountTransferFilter(
  /** 이체 일시 범위 */
  val tradeTimestampRange: DateTimeRange? = null,
  /** 생성 일시 범위 */
  val createdTimestampRange: DateTimeRange? = null,
  /** 상태 업데이트 일시 범위 */
  val statusUpdatedTimestampRange: DateTimeRange? = null,
  /** 이체 예정 일시 범위 */
  val scheduledTimestampRange: DateTimeRange? = null,
  /** 이체 아이디 */
  val accountTransferId: String? = null,
  /** 계좌 아이디 */
  val bankAccountId: String? = null,
  /** 일괄 이체 아이디 */
  val bulkAccountTransferId: String? = null,
  /** 지급 아이디 */
  val payoutId: String? = null,
  /** 이체 아이디 리스트 */
  val accountTransferIds: List<String>? = null,
  /** 구분 */
  val types: List<PlatformAccountTransferType>? = null,
  /** 상태 */
  val statuses: List<PlatformAccountTransferStatus>? = null,
  /** 입금자명 */
  val depositorName: String? = null,
  /** 예금주 */
  val depositAccountHolder: String? = null,
  /** 받는 이 통장 메모 */
  val depositMemo: String? = null,
  /** 보내는 이 통장 메모 */
  val withdrawalMemo: String? = null,
)


