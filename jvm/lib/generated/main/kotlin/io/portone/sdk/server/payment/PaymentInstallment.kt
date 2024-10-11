package io.portone.sdk.server.payment

import kotlinx.serialization.Serializable

/** 할부 정보 */
@Serializable
public data class PaymentInstallment(
  /** 할부 개월 수 */
  val month: Int,
  /** 무이자할부 여부 */
  val isInterestFree: Boolean,
)
