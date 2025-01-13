package io.portone.sdk.server.payment

import io.portone.sdk.server.payment.PaymentTransaction
import kotlinx.serialization.Serializable

/** 결제 시도 내역 조회 응답 정보 */
@Serializable
public data class GetPaymentTransactionsResponse(
  /** 결제 시도 내역 */
  val items: List<PaymentTransaction>,
)


