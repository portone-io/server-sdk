package io.portone.sdk.server.b2b.counterparty

import kotlin.String
import kotlinx.serialization.Serializable

/** 거래처 담당자 입력 정보 */
@Serializable
public data class B2bCounterpartyContactInput(
  /** 담당자 성명 */
  val name: String,
  /** 담당자 전화번호 */
  val phoneNumber: String? = null,
  /** 담당자 이메일 */
  val email: String,
  /** 담당자 메모 */
  val memo: String? = null,
)


