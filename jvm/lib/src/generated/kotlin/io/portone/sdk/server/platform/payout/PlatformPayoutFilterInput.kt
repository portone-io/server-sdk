package io.portone.sdk.server.platform.payout

import io.portone.sdk.server.common.Bank
import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.platform.payout.PlatformPayoutFilterInputCriteria
import io.portone.sdk.server.platform.payout.PlatformPayoutStatus
import kotlin.Array
import kotlin.String
import kotlinx.serialization.Serializable

/** 지급 내역 필터 입력 정보 */
@Serializable
public data class PlatformPayoutFilterInput(
  /**
   * 지급 상태
   *
   * 값이 존재하는 경우 해당 리스트에 포함되는 지급 상태를 가진 지급 내역을 조회합니다.
   */
  val statuses: List<PlatformPayoutStatus>? = null,
  /**
   * 파트너 아이디
   *
   * 값이 존재하는 경우 해당 리스트에 포함되는 파트너 아이디를 가진 지급 내역을 조회합니다.
   */
  val partnerIds: List<String>? = null,
  /** 조회 기준 */
  val criteria: PlatformPayoutFilterInputCriteria,
  /**
   * 지급 계좌 은행
   *
   * 값이 존재하는 경우 해당 리스트에 포함되는 지급 계좌 은행을 가진 지급 내역을 조회합니다.
   */
  val payoutAccountBanks: List<Bank>? = null,
  /**
   * 파트너 태그
   *
   * 값이 존재하는 경우 해당 리스트에 포함되는 파트너 태그를 하나 이상 가진 지급 내역을 조회합니다.
   */
  val partnerTags: List<String>? = null,
  /**
   * 지급 통화
   *
   * 값이 존재하는 경우 해당 리스트에 포함되는 지급 통화를 가진 지급 내역을 조회합니다.
   */
  val payoutCurrencies: List<Currency>? = null,
)


