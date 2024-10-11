package io.portone.sdk.server.paymentschedule

import io.portone.sdk.server.common.PageInfo
import io.portone.sdk.server.paymentschedule.PaymentSchedule
import kotlinx.serialization.Serializable

/** 결제 예약 다건 조회 성공 응답 정보 */
@Serializable
public data class GetPaymentSchedulesResponse(
  /** 조회된 결제 예약 건 리스트 */
  val items: List<PaymentSchedule>,
  /** 조회된 페이지 정보 */
  val page: PageInfo,
)
