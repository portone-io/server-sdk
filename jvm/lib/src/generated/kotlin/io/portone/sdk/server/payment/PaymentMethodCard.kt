package io.portone.sdk.server.payment

import io.portone.sdk.server.common.Card
import io.portone.sdk.server.payment.PaymentInstallment
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 결제수단 카드 정보 */
@Serializable
@SerialName("PaymentMethodCard")
public data class PaymentMethodCard(
  /** 카드 상세 정보 */
  val card: Card? = null,
  /** 승인 번호 */
  val approvalNumber: String? = null,
  /** 할부 정보 */
  val installment: PaymentInstallment? = null,
  /** 카드 포인트 사용여부 */
  val pointUsed: Boolean? = null,
) : PaymentMethod.Recognized, PaymentMethodEasyPayMethod.Recognized


