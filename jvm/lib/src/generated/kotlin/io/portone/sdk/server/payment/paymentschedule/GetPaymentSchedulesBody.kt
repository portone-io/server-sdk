package io.portone.sdk.server.payment.paymentschedule

import io.portone.sdk.server.common.PageInput
import io.portone.sdk.server.payment.paymentschedule.PaymentScheduleFilterInput
import io.portone.sdk.server.payment.paymentschedule.PaymentScheduleSortInput
import kotlinx.serialization.Serializable

/**
 * 결제 예약 다건 조회를 위한 입력 정보
 *
 * 조회 결과는 결제 예정 시점(timeToPay) 기준 최신 순으로 정렬됩니다.
 */
@Serializable
internal data class GetPaymentSchedulesBody(
  /**
   * 요청할 페이지 정보
   *
   * 미 입력 시 number: 0, size: 10 으로 기본값이 적용됩니다.
   */
  val page: PageInput? = null,
  /**
   * 정렬 조건
   *
   * 미 입력 시 sortBy: TIME_TO_PAY, sortOrder: DESC 으로 기본값이 적용됩니다.
   */
  val sort: PaymentScheduleSortInput? = null,
  /** 조회할 결제 예약 건의 조건 필터 */
  val filter: PaymentScheduleFilterInput? = null,
)
