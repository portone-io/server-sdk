package io.portone.sdk.server.pgspecific

import kotlin.String
import kotlinx.serialization.Serializable

/** 카카오페이 주문 조회 응답 */
@Serializable
public data class GetKakaopayPaymentOrderResponse(
  /** HTTP 상태 코드 */
  val statusCode: Int,
  /** HTTP 응답 본문 (JSON) */
  val body: String,
)
