package io.portone.sdk.server.payment

import io.portone.sdk.server.payment.PaymentEvent
import kotlin.String
import kotlinx.serialization.Serializable

/** 결제 이벤트 및 커서 정보 */
@Serializable
public data class PaymentEventWithCursor(
  /** 결제 이벤트 정보 */
  val paymentEvent: PaymentEvent,
  /** 해당 결제 이벤트의 커서 정보 */
  val cursor: String,
)


