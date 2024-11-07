package io.portone.sdk.server.payment

import kotlinx.serialization.Serializable

/** 결제 건 정렬 기준 */
@Serializable
public enum class PaymentSortBy {
  /** 결제 요청 시점 */
  RequestedAt,
  /** 상태 변경 시점 */
  StatusChangedAt,
}
