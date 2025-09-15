package io.portone.sdk.server.payment

import io.portone.sdk.server.payment.PaymentEventWithCursor
import kotlinx.serialization.Serializable

/** 결제 이벤트 커서 기반 대용량 다건 조회 성공 응답 정보 */
@Serializable
public data class GetAllPaymentEventsByCursorResponse(
  /** 조회된 결제 이벤트 및 커서 정보 리스트 */
  val items: List<PaymentEventWithCursor>,
)


