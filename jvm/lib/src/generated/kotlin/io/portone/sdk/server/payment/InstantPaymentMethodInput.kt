package io.portone.sdk.server.payment

import io.portone.sdk.server.payment.InstantPaymentMethodInputCard
import io.portone.sdk.server.payment.InstantPaymentMethodInputVirtualAccount
import kotlinx.serialization.Serializable

/**
 * 수기 결제 수단 입력 정보
 *
 * 하나의 필드만 입력합니다.
 */
@Serializable
public data class InstantPaymentMethodInput(
  /** 카드 */
  val card: InstantPaymentMethodInputCard? = null,
  /** 가상계좌 */
  val virtualAccount: InstantPaymentMethodInputVirtualAccount? = null,
)


