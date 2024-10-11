package io.portone.sdk.server.platform.transfer

import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.platform.transfer.PlatformPaymentMethodInput
import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlin.String
import kotlinx.serialization.Serializable

/** 외부 결제 상세 정보 */
@Serializable
public data class CreatePlatformOrderTransferBodyExternalPaymentDetail(
  /** 통화 */
  val currency: Currency,
  /** 주문 명 */
  val orderName: String? = null,
  /** 결제 일시 */
  val paidAt: @Serializable(InstantSerializer::class) Instant? = null,
  /** 결제 수단 */
  val method: PlatformPaymentMethodInput? = null,
)
