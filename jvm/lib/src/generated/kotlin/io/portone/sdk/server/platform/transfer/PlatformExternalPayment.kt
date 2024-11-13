package io.portone.sdk.server.platform.transfer

import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.platform.transfer.PlatformPaymentMethod
import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 외부 결제 정보 */
@Serializable
@SerialName("EXTERNAL")
public data class PlatformExternalPayment(
  /** 결제 아이디 */
  val id: String,
  /** 통화 */
  val currency: Currency,
  /** 주문 명 */
  val orderName: String? = null,
  /** 결제 수단 */
  val method: PlatformPaymentMethod? = null,
  /** 결제 일시 */
  val paidAt: @Serializable(InstantSerializer::class) Instant? = null,
) : PlatformPayment
