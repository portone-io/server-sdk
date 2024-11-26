package io.portone.sdk.server.payment.billingkey

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 모바일 정보 */
@Serializable
@SerialName("BillingKeyPaymentMethodMobile")
public data class BillingKeyPaymentMethodMobile(
  /** 전화번호 */
  val phoneNumber: String? = null,
) : BillingKeyPaymentMethod.Recognized


