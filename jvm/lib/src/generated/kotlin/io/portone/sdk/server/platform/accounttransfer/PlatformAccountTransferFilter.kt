package io.portone.sdk.server.platform.accounttransfer

import io.portone.sdk.server.common.DateTimeRange
import io.portone.sdk.server.platform.accounttransfer.PlatformAccountTransferType
import io.portone.sdk.server.platform.accounttransfer.Status
import kotlin.String
import kotlinx.serialization.Serializable

@Serializable
public data class PlatformAccountTransferFilter(
  /** 거래 시간 범위 */
  val tradeTimestampRange: DateTimeRange? = null,
  /** 이체 아이디 */
  val accountTransferId: String? = null,
  /** 구분 */
  val types: List<PlatformAccountTransferType>? = null,
  /** 상태 */
  val statuses: List<Status>? = null,
  /** 입금자명 */
  val depositorName: String? = null,
  /** 예금주 */
  val depositAccountHolder: String? = null,
  /** 받는 이 통장 메모 */
  val depositMemo: String? = null,
  /** 보내는 이 통장 메모 */
  val withdrawalMemo: String? = null,
)


