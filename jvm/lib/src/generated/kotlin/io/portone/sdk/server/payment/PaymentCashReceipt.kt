package io.portone.sdk.server.payment

import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

/** 결제 건 내 현금영수증 정보 */
@Serializable
@JsonClassDiscriminator("status")
public sealed interface PaymentCashReceipt {
}
