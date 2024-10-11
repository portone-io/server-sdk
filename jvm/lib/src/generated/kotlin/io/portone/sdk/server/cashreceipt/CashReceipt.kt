package io.portone.sdk.server.cashreceipt

import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

/** 현금영수증 내역 */
@Serializable
@JsonClassDiscriminator("status")
public sealed interface CashReceipt {
}
