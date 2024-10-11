package io.portone.sdk.server.payment

import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

/** 결제 건 */
@Serializable
@JsonClassDiscriminator("status")
public sealed interface Payment {
}
