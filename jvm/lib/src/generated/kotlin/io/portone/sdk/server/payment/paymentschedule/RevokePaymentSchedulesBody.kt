package io.portone.sdk.server.payment.paymentschedule

import kotlin.Array
import kotlin.String
import kotlinx.serialization.Serializable

/**
 * 결제 예약 건 취소 요청 입력 정보
 *
 * billingKey, scheduleIds 중 하나 이상은 필수로 입력합니다.
 * billingKey 만 입력된 경우 -> 해당 빌링키로 예약된 모든 결제 예약 건들이 취소됩니다.
 * scheduleIds 만 입력된 경우 -> 입력된 결제 예약 건 아이디에 해당하는 예약 건들이 취소됩니다.
 * billingKey, scheduleIds 모두 입력된 경우 -> 입력된 결제 예약 건 아이디에 해당하는 예약 건들이 취소됩니다. 그리고 예약한 빌링키가 입력된 빌링키와 일치하는지 검증합니다.
 * 위 정책에 따라 선택된 결제 예약 건들 중 하나라도 취소에 실패할 경우, 모든 취소 요청이 실패합니다.
 */
@Serializable
internal data class RevokePaymentSchedulesBody(
  /**
   * 상점 아이디
   *
   * 접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
   */
  val storeId: String? = null,
  /** 빌링키 */
  val billingKey: String? = null,
  /** 결제 예약 건 아이디 목록 */
  val scheduleIds: List<String>? = null,
)
