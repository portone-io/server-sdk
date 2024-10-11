package io.portone.sdk.server.platform.accounttransfer

import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

/**
 * 계좌 이체
 *
 * 송금 대행을 통해 일어난 정산 금액 지급, 인출 목적의 계좌 이체 결과 정보입니다.
 */
@Serializable
@JsonClassDiscriminator("type")
public sealed interface PlatformAccountTransfer {
}
