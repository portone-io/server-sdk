package io.portone.sdk.server.platform.partnersettlement

import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.platform.DateRange
import io.portone.sdk.server.platform.PlatformContract
import io.portone.sdk.server.platform.PlatformOrderSettlementAmount
import io.portone.sdk.server.platform.PlatformPartner
import io.portone.sdk.server.platform.partnersettlement.PlatformPartnerSettlement
import io.portone.sdk.server.platform.partnersettlement.PlatformPartnerSettlementStatus
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("ORDER")
public data class PlatformPartnerOrderSettlement(
  /** 정산내역 아이디 */
  override val id: String,
  override val graphqlId: String,
  /** 파트너 */
  override val partner: PlatformPartner,
  /**
   * 정산 일
   *
   * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
   */
  override val settlementDate: String,
  /** 정산 통화 */
  override val settlementCurrency: Currency,
  /** 정산 상태 */
  override val status: PlatformPartnerSettlementStatus,
  /** 계약 */
  val contract: PlatformContract,
  /** 정산 시작 일 범위 */
  val settlementStartDateRange: DateRange,
  /** 금액 정보 */
  val amount: PlatformOrderSettlementAmount,
  /** 테스트 모드 여부 */
  override val isForTest: Boolean,
  /** 메모 */
  override val memo: String? = null,
): PlatformPartnerSettlement
