package io.portone.sdk.server.b2b.counterparty

import io.portone.sdk.server.b2b.counterparty.B2bCounterpartyCreateOptions
import io.portone.sdk.server.b2b.counterparty.B2bCounterpartyInput
import kotlin.String
import kotlinx.serialization.Serializable

/** 거래처 생성 요청 정보 */
@Serializable
internal data class CreateB2bCounterpartyBody(
  /**
   * 거래처 아이디
   *
   * 입력하지 않으면 임의의 ID가 채번됩니다.
   */
  val counterpartyId: String? = null,
  /** 거래처 정보 */
  val counterparty: B2bCounterpartyInput,
  /** 거래처 생성 옵션 */
  val options: B2bCounterpartyCreateOptions? = null,
)


