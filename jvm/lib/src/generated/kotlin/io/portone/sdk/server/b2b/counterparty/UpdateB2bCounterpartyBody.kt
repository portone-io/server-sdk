package io.portone.sdk.server.b2b.counterparty

import io.portone.sdk.server.b2b.counterparty.B2bCounterpartyCreateOptions
import io.portone.sdk.server.b2b.counterparty.B2bCounterpartyInput
import kotlinx.serialization.Serializable

/** 거래처 정보 수정 요청 */
@Serializable
internal data class UpdateB2bCounterpartyBody(
  /** 거래처 정보 */
  val counterparty: B2bCounterpartyInput,
  /**
   * 확인 옵션
   *
   * 사업자 정보 및 휴폐업 상태 조회 옵션입니다.
   */
  val options: B2bCounterpartyCreateOptions? = null,
)


