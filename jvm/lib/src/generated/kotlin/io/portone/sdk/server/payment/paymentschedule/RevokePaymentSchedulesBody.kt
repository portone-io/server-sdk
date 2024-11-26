package io.portone.sdk.server.payment.paymentschedule

import kotlin.Array
import kotlin.String
import kotlinx.serialization.Serializable

/** 결제 예약 건 취소 요청 입력 정보 */
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


