package io.portone.sdk.server.payment

import kotlinx.serialization.Serializable

/** 결제 건 상태 */
@Serializable
public enum class PaymentStatus {
  Ready,
  Pending,
  VirtualAccountIssued,
  Paid,
  Failed,
  PartialCancelled,
  Cancelled,
}
