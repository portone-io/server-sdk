package io.portone.sdk.server.platform

import io.portone.sdk.server.platform.SettlementAmountType
import kotlin.String
import kotlinx.serialization.Serializable

/** 플랫폼 설정 업데이트를 위한 입력 정보 */
@Serializable
internal data class UpdatePlatformSettingBody(
  /** 기본 보내는 이 통장 메모 */
  val defaultWithdrawalMemo: String? = null,
  /** 기본 받는 이 통장 메모 */
  val defaultDepositMemo: String? = null,
  /** paymentId, storeId, partnerId가 같은 주문 정산건에 대한 중복 정산 지원 여부 */
  val supportsMultipleOrderTransfersPerPartner: Boolean? = null,
  /** 정산일이 정산시작일보다 작거나 같을 경우 공휴일 후 영업일로 정산일 다시 계산 여부 */
  val adjustSettlementDateAfterHolidayIfEarlier: Boolean? = null,
  /** 지급 금액에서 원천징수세 차감 여부 */
  val deductWht: Boolean? = null,
  /** 정산 금액 취급 기준 */
  val settlementAmountType: SettlementAmountType? = null,
)


