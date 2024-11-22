package io.portone.sdk.server.payment

import kotlin.String
import kotlinx.serialization.Serializable

/** 결제 실패 정보 */
@Serializable
public data class PaymentFailure(
  /** 실패 사유 */
  val reason: String? = null,
  /** PG사 실패 코드 */
  val pgCode: String? = null,
  /** PG사 실패 메시지 */
  val pgMessage: String? = null,
)


