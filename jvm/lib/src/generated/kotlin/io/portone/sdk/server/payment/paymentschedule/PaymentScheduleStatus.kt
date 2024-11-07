package io.portone.sdk.server.payment.paymentschedule

import kotlinx.serialization.Serializable

/** 결제 예약 건 상태 */
@Serializable
public enum class PaymentScheduleStatus {
  /** 예약 완료 */
  Scheduled,
  /** 결제 시작 */
  Started,
  /** 결제 성공 */
  Succeeded,
  /** 결제 실패 */
  Failed,
  /** 취소된 결제 예약 */
  Revoked,
  /** 결제 승인 대기 */
  Pending,
}
