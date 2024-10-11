package io.portone.sdk.server.platform.transfer

import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.platform.transfer.PlatformPaymentMethod
import kotlin.String
import kotlinx.datetime.Instant
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 외부 결제 정보 */
@Serializable
@SerialName("EXTERNAL")
public data class PlatformExternalPayment(
  /** 결제 아이디 */
  override val id: String,
  /** 통화 */
  override val currency: Currency,
  /** 주문 명 */
  override val orderName: String? = null,
  /** 결제 수단 */
  override val method: PlatformPaymentMethod? = null,
  /** 결제 일시 */
  override val paidAt: Instant? = null,
): PlatformPayment,
