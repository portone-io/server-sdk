package io.portone.sdk.server.platform.transfer

import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.platform.transfer.PlatformPaymentMethod
import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 포트원 결제 정보 */
@Serializable
@SerialName("PORT_ONE")
public data class PlatformPortOnePayment(
  /** 결제 아이디 */
  override val id: String,
  /** 상점 아이디 */
  val storeId: String,
  /** 채널 키 */
  val channelKey: String,
  /** 주문 명 */
  override val orderName: String,
  /** 결제 수단 */
  override val method: PlatformPaymentMethod? = null,
  /** 통화 */
  override val currency: Currency,
  /** 결제 일시 */
  override val paidAt: @Serializable(InstantSerializer::class) Instant,
) : PlatformPayment.Recognized


