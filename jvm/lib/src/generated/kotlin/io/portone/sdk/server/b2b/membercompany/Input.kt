package io.portone.sdk.server.b2b.membercompany

import io.portone.sdk.server.common.Bank
import kotlin.String
import kotlinx.serialization.Serializable

@Serializable
internal data class Input(
  /** 은행 */
  val bank: Bank,
  /** 계좌번호 */
  val accountNumber: String,
)
