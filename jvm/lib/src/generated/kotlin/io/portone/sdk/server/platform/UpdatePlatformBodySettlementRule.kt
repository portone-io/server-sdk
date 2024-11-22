package io.portone.sdk.server.platform

import kotlinx.serialization.Serializable

/**
 * 플랫폼 업데이트 시 변경할 정산 규칙 정보
 *
 * 값이 명시되지 않은 필드는 업데이트하지 않습니다.
 */
@Serializable
public data class UpdatePlatformBodySettlementRule(
  /** paymentId, storeId, partnerId가 같은 주문 정산건에 대한 중복 정산 지원 여부 */
  val supportsMultipleOrderTransfersPerPartner: Boolean? = null,
  /** 정산일이 정산시작일보다 작거나 같을 경우 공휴일 후 영업일로 정산일 다시 계산 여부 */
  val adjustSettlementDateAfterHolidayIfEarlier: Boolean? = null,
  /** 지급 금액에서 원천징수세 차감 여부 */
  val subtractWhtInPayoutAmount: Boolean? = null,
)


