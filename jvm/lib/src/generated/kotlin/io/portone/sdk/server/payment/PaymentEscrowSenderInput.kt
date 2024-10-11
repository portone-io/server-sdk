package io.portone.sdk.server.payment

import io.portone.sdk.server.common.SeparatedAddressInput
import kotlin.String
import kotlinx.serialization.Serializable

/** 에스크로 발송자 정보 */
@Serializable
public data class PaymentEscrowSenderInput(
  /** 이름 */
  val name: String? = null,
  /** 전화번호 */
  val phoneNumber: String? = null,
  /** 우편번호 */
  val zipcode: String? = null,
  /** 수취인과의 관계 */
  val relationship: String? = null,
  /** 주소 */
  val address: SeparatedAddressInput? = null,
)
