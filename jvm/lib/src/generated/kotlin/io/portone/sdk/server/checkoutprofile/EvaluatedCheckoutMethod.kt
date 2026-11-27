package io.portone.sdk.server.checkoutprofile

import io.portone.sdk.server.common.CheckoutPaymentMethod
import kotlin.String
import kotlinx.serialization.Serializable

/** 결제 수단 */
@Serializable
public data class EvaluatedCheckoutMethod(
  /** 결제수단 */
  val paymentMethod: CheckoutPaymentMethod,
  /** 채널 키 */
  val channelKey: String,
)


