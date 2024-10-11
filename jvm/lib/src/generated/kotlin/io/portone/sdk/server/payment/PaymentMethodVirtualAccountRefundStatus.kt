package io.portone.sdk.server.payment

import kotlinx.serialization.Serializable

/** 가상계좌 환불 상태 */
@Serializable
public enum class PaymentMethodVirtualAccountRefundStatus {
  /** 처리중 */
  PENDING,
  /** 부분 환불 실패 */
  PARTIAL_REFUND_FAILED,
  /** 환불 실패 */
  FAILED,
  /** 환불 완료 */
  COMPLETED,
}
