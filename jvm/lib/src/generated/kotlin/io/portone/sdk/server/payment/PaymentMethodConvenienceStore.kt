package io.portone.sdk.server.payment

import io.portone.sdk.server.payment.ConvenienceStoreBrand
import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 편의점 결제 상세 정보 */
@Serializable
@SerialName("PaymentMethodConvenienceStore")
public data class PaymentMethodConvenienceStore(
  /** 편의점 브랜드 */
  val convenienceStoreBrand: ConvenienceStoreBrand? = null,
  /** 결제 확인 번호 */
  val confirmationNumber: String? = null,
  /** 결제 접수 번호 */
  val receiptNumber: String? = null,
  /** 결제 마감 시간 */
  val paymentDeadline: @Serializable(InstantSerializer::class) Instant? = null,
) : PaymentMethod.Recognized


