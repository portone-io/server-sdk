package io.portone.sdk.server.payment

import io.portone.sdk.server.payment.PaymentEscrow
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 배송 정보 등록 전 */
@Serializable
@SerialName("BEFORE_REGISTERED")
public data object BeforeRegisteredPaymentEscrow: PaymentEscrow
