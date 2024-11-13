package io.portone.sdk.server.payment

import io.portone.sdk.server.common.Bank
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 계좌 이체 상세 정보 */
@Serializable
@SerialName("PaymentMethodTransfer")
public data class PaymentMethodTransfer(
  /** 표준 은행 코드 */
  val bank: Bank? = null,
) : PaymentMethod, PaymentMethodEasyPayMethod
