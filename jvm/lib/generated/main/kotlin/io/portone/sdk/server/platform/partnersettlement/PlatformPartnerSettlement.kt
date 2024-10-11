package io.portone.sdk.server.platform.partnersettlement

import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.platform.PlatformPartner
import io.portone.sdk.server.platform.partnersettlement.PlatformPartnerSettlementStatus
import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

@Serializable
@JsonClassDiscriminator("type")
public sealed interface PlatformPartnerSettlement {
  /** 정산내역 아이디 */
  val id: String
  val graphqlId: String
  /** 파트너 */
  val partner: PlatformPartner
  /**
   * 정산 일
   *
   * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
   */
  val settlementDate: String
  /** 정산 통화 */
  val settlementCurrency: Currency
  /** 정산 상태 */
  val status: PlatformPartnerSettlementStatus
  /** 메모 */
  val memo: String?
  /** 정산 금액 */
  val amount: Long
  /** 테스트 모드 여부 */
  val isForTest: Boolean
}
