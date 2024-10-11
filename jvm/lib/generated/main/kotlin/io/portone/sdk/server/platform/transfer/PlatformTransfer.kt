package io.portone.sdk.server.platform.transfer

import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.platform.PlatformPartner
import io.portone.sdk.server.platform.transfer.PlatformTransferStatus
import io.portone.sdk.server.platform.transfer.PlatformUserDefinedPropertyKeyValue
import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

/**
 * 정산건
 *
 * 정산건은 파트너에 정산해줄 정산 금액과 정산 방식 등이 포함되어 있는 정산 정보입니다.
 * 정산 방식은은 주문 정산, 주문 취소 정산, 수기 정산이 있습니다.
 */
@Serializable
@JsonClassDiscriminator("type")
public sealed interface PlatformTransfer {
  /** 정산건 아이디 */
  val id: String
  val graphqlId: String
  /** 파트너 */
  val partner: PlatformPartner
  /** 정산 상태 */
  val status: PlatformTransferStatus
  /** 메모 */
  val memo: String?
  /**
   * 정산 일
   *
   * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
   */
  val settlementDate: String
  /** 정산 통화 */
  val settlementCurrency: Currency
  val payoutId: String?
  val payoutGraphqlId: String?
  /** 테스트 모드 여부 */
  val isForTest: Boolean
  /** 사용자 정의 속성 */
  val userDefinedProperties: Array<PlatformUserDefinedPropertyKeyValue>
}
