package io.portone.sdk.server.paymentschedule

import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

/** 결제 예약 건 */
@Serializable
@JsonClassDiscriminator("status")
public sealed interface PaymentSchedule {
}
