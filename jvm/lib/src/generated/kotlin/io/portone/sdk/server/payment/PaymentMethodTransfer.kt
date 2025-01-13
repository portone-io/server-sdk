package io.portone.sdk.server.payment

import io.portone.sdk.server.common.Bank
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 계좌 이체 상세 정보 */
@Serializable
@SerialName("PaymentMethodTransfer")
public data class PaymentMethodTransfer(
  /** 표준 은행 코드 */
  val bank: Bank? = null,
  /** 계좌번호 */
  val accountNumber: String? = null,
) : PaymentMethod.Recognized, PaymentMethodEasyPayMethod.Recognized


