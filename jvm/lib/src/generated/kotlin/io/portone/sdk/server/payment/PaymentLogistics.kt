package io.portone.sdk.server.payment

import io.portone.sdk.server.common.SeparatedAddressInput
import io.portone.sdk.server.payment.PaymentLogisticsCompany
import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlin.String
import kotlinx.serialization.Serializable

/** 배송정보 */
@Serializable
public data class PaymentLogistics(
  /** 물류회사 */
  val company: PaymentLogisticsCompany,
  /** 송장번호 */
  val invoiceNumber: String,
  /** 발송시점 */
  val sentAt: @Serializable(InstantSerializer::class) Instant,
  /** 수령시점 */
  val receivedAt: @Serializable(InstantSerializer::class) Instant? = null,
  /** 주소 */
  val address: SeparatedAddressInput? = null,
)
