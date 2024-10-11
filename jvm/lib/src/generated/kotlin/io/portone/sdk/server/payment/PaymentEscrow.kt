package io.portone.sdk.server.payment

import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

/**
 * 에스크로 정보
 *
 * V1 결제 건의 경우 타입이 REGISTERED 로 고정됩니다.
 */
@Serializable
@JsonClassDiscriminator("status")
public sealed interface PaymentEscrow {
}
