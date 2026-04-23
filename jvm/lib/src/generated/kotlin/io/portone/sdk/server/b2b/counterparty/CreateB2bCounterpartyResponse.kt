package io.portone.sdk.server.b2b.counterparty

import io.portone.sdk.server.b2b.counterparty.B2bCounterparty
import kotlinx.serialization.Serializable

/** 거래처 생성 응답 정보 */
@Serializable
public data class CreateB2bCounterpartyResponse(
  /** 거래처 정보 */
  val counterparty: B2bCounterparty,
)


