package io.portone.sdk.server.platform.transfer

import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.platform.PlatformContract
import io.portone.sdk.server.platform.PlatformOrderSettlementAmount
import io.portone.sdk.server.platform.PlatformPartner
import io.portone.sdk.server.platform.transfer.PlatformOrderTransferAdditionalFee
import io.portone.sdk.server.platform.transfer.PlatformOrderTransferCancellation
import io.portone.sdk.server.platform.transfer.PlatformOrderTransferDiscount
import io.portone.sdk.server.platform.transfer.PlatformOrderTransferOrderLine
import io.portone.sdk.server.platform.transfer.PlatformPayment
import io.portone.sdk.server.platform.transfer.PlatformTransferStatus
import io.portone.sdk.server.platform.transfer.PlatformUserDefinedPropertyKeyValue
import io.portone.sdk.server.platform.transfer.TransferParameters
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 주문 취소 정산건 */
@Serializable
@SerialName("ORDER_CANCEL")
public data class PlatformOrderCancelTransfer(
  /** 정산건 아이디 */
  val id: String,
  val graphqlId: String,
  /** 파트너 */
  val partner: PlatformPartner,
  /** 정산 상태 */
  val status: PlatformTransferStatus,
  /**
   * 정산 일
   *
   * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
   */
  val settlementDate: String,
  /** 정산 통화 */
  val settlementCurrency: Currency,
  /** 테스트 모드 여부 */
  val isForTest: Boolean,
  /** 사용자 정의 속성 */
  val userDefinedProperties: List<PlatformUserDefinedPropertyKeyValue>,
  /** 정산 금액 정보 */
  val amount: PlatformOrderSettlementAmount,
  /** 계약 */
  val contract: PlatformContract,
  /** 결제 정보 */
  val payment: PlatformPayment,
  /**
   * 정산 시작일
   *
   * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
   */
  val settlementStartDate: String,
  /** 주문 항목 리스트 */
  val orderLines: List<PlatformOrderTransferOrderLine>,
  /** 정산 금액 계산 시 사용된 추가 수수료 정보 */
  val additionalFees: List<PlatformOrderTransferAdditionalFee>,
  /** 정산 금액 계산 시 사용된 할인 정보 */
  val discounts: List<PlatformOrderTransferDiscount>,
  /** 주문 취소 정보 */
  val cancellation: PlatformOrderTransferCancellation,
  /** 정산 파라미터 (실험기능) */
  val parameters: TransferParameters,
  /** 메모 */
  val memo: String? = null,
  val payoutId: String? = null,
  val payoutGraphqlId: String? = null,
) : PlatformTransfer
