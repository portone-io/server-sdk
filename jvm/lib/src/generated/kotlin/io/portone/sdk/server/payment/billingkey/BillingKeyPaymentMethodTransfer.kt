package io.portone.sdk.server.payment.billingkey

import io.portone.sdk.server.common.Bank
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 계좌이체 정보 */
@Serializable
@SerialName("BillingKeyPaymentMethodTransfer")
public data class BillingKeyPaymentMethodTransfer(
  /** 표준 은행 코드 */
  val bank: Bank? = null,
  /** 계좌번호 */
  val accountNumber: String? = null,
) : BillingKeyPaymentMethod.Recognized, BillingKeyPaymentMethodEasyPayMethod.Recognized


