package io.portone.sdk.server.platform.transfer

import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

/**
 * 정산건
 *
 * 정산건은 파트너에 정산해줄 정산 금액과 정산 방식 등이 포함되어 있는 정산 정보입니다.
 * 정산 방식은은 주문 정산, 주문 취소 정산, 수기 정산이 있습니다.
 */
@Serializable
@JsonClassDiscriminator("type")
public sealed interface PlatformTransfer {
}
