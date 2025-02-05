package io.portone.sdk.server.payment

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 편의점 결제 상세 정보 */
@Serializable
@SerialName("PaymentMethodConvenienceStore")
public data object PaymentMethodConvenienceStore : PaymentMethod.Recognized


