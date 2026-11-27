package io.portone.sdk.server.paymentsession

import kotlin.String
import kotlinx.serialization.Serializable

/** 결제 세션 약관 */
@Serializable
public data class PaymentSessionAgreement(
  /** 약관 이름 */
  val name: String,
  /** 약관 URL */
  val url: String,
)


