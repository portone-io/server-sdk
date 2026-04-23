package io.portone.sdk.server.payment

import io.portone.sdk.server.payment.PaymentOriginPlatformType
import kotlin.String
import kotlinx.serialization.Serializable

/** 결제 출처 정보 */
@Serializable
public data class PaymentOrigin(
  /** 결제를 요청한 플랫폼 타입 */
  val platformType: PaymentOriginPlatformType,
  /** 결제를 요청한 user agent 문자열 */
  val userAgent: String? = null,
  /** 결제를 요청한 페이지 URL */
  val url: String? = null,
  /** 결제를 요청한 IP 주소 */
  val ipAddress: String,
)


