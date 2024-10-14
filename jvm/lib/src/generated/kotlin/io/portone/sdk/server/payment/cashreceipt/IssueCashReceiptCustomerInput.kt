package io.portone.sdk.server.payment.cashreceipt

import kotlin.String
import kotlinx.serialization.Serializable

/** 현금영수증 발급 시 고객 관련 입력 정보 */
@Serializable
public data class IssueCashReceiptCustomerInput(
  /** 고객 식별값 */
  val identityNumber: String,
  /** 이름 */
  val name: String? = null,
  /** 이메일 */
  val email: String? = null,
  /** 전화번호 */
  val phoneNumber: String? = null,
)
