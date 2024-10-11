package io.portone.sdk.server.payment

import io.portone.sdk.server.common.EasyPayProvider
import io.portone.sdk.server.payment.PaymentMethodEasyPayMethod
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 간편 결제 상세 정보 */
@Serializable
@SerialName("PaymentMethodEasyPay")
public data class PaymentMethodEasyPay(
  /** 간편 결제 PG사 */
  val provider: EasyPayProvider? = null,
  /** 간편 결제 수단 */
  val easyPayMethod: PaymentMethodEasyPayMethod? = null,
): PaymentMethod,
