package io.portone.sdk.server.b2b.counterparty

import io.portone.sdk.server.b2b.counterparty.B2bCounterparty
import kotlinx.serialization.Serializable

/** 거래처 정보 수정 응답 */
@Serializable
public data class UpdateB2bCounterpartyResponse(
  /** 거래처 정보 */
  val counterparty: B2bCounterparty,
)


