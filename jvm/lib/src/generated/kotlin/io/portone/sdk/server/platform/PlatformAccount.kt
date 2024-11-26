package io.portone.sdk.server.platform

import io.portone.sdk.server.common.Bank
import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.platform.PlatformAccountStatus
import kotlin.String
import kotlinx.serialization.Serializable

/**
 * 플랫폼 정산 계좌
 *
 * `currency` 가 KRW 일 경우 예금주 조회 API 를 통해 올바른 계좌인지 검증합니다. 그 외의 화폐일 경우 따로 검증하지는 않습니다.
 */
@Serializable
public data class PlatformAccount(
  /** 은행 */
  val bank: Bank,
  /** 정산에 사용할 통화 */
  val currency: Currency,
  /** 계좌번호 */
  val number: String,
  /** 예금주명 */
  val holder: String,
  /** 계좌 상태 */
  val status: PlatformAccountStatus,
)


