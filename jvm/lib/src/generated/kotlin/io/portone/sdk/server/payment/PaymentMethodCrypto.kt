package io.portone.sdk.server.payment

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 암호화폐 결제 상세 정보 */
@Serializable
@SerialName("PaymentMethodCrypto")
public data object PaymentMethodCrypto : PaymentMethod.Recognized


