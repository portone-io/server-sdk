package io.portone.sdk.server.payment

import io.portone.sdk.server.payment.PaymentEscrow
import java.time.Instant
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 배송 완료 */
@Serializable
@SerialName("DELIVERED")
public data class DeliveredPaymentEscrow(
  /** 택배사 */
  val company: String,
  /** 송장번호 */
  val invoiceNumber: String,
  /** 발송 일시 */
  val sentAt: Instant? = null,
  /** 배송등록 처리 일자 */
  val appliedAt: Instant? = null,
): PaymentEscrow
