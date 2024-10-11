package io.portone.sdk.server.b2b

import kotlin.String
import kotlinx.serialization.Serializable

/** 예금주 조회 응답 정보 */
@Serializable
public data class GetB2bBankAccountHolderResponse(
  /** 예금주 */
  val accountHolder: String,
)
