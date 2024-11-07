package io.portone.sdk.server.payment

import kotlinx.serialization.Serializable

/** 에스크로 상태 */
@Serializable
public enum class PaymentFilterInputEscrowStatus {
  Registered,
  Delivered,
  Confirmed,
  Rejected,
  Cancelled,
  RejectConfirmed,
}
