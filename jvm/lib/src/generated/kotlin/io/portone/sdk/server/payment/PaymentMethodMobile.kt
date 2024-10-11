package io.portone.sdk.server.payment

import io.portone.sdk.server.payment.PaymentMethod
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 모바일 상세 정보 */
@Serializable
@SerialName("PaymentMethodMobile")
public data class PaymentMethodMobile(
  /** 전화번호 */
  val phoneNumber: String? = null,
): PaymentMethod
