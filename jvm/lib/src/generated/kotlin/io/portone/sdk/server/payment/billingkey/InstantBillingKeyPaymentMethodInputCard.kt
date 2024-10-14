package io.portone.sdk.server.payment.billingkey

import io.portone.sdk.server.common.CardCredential
import kotlinx.serialization.Serializable

/** 카드 수단 정보 입력 양식 */
@Serializable
public data class InstantBillingKeyPaymentMethodInputCard(
  val credential: CardCredential,
)
