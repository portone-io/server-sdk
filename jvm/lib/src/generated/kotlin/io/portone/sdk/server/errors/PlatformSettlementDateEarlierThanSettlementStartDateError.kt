package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 정산일이 정산 시작일보다 빠른 경우 */
@Serializable
@SerialName("PLATFORM_SETTLEMENT_DATE_EARLIER_THAN_SETTLEMENT_START_DATE")
internal data class PlatformSettlementDateEarlierThanSettlementStartDateError(
  override val message: String? = null,
  /**
   * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
   * (yyyy-MM-dd)
   */
  val settlementStartDate: String,
  /**
   * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
   * (yyyy-MM-dd)
   */
  val settlementDate: String,
) : CreatePlatformOrderCancelTransferError.Recognized, CreatePlatformOrderTransferError.Recognized


