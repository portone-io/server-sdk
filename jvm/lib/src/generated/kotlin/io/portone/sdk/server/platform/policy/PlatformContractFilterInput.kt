package io.portone.sdk.server.platform.policy

import io.portone.sdk.server.platform.PlatformPayer
import io.portone.sdk.server.platform.PlatformSettlementCycleDatePolicy
import io.portone.sdk.server.platform.policy.PlatformContractFilterInputKeyword
import io.portone.sdk.server.platform.policy.PlatformSettlementCycleType
import kotlinx.serialization.Serializable

/** 계약 다건 조회를 위한 필터 조건 */
@Serializable
public data class PlatformContractFilterInput(
  /**
   * 금액 부담 주체
   *
   * 하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 수수료 부담 주체를 가진 계약만 조회합니다.
   */
  val platformFeePayers: List<PlatformPayer>? = null,
  /**
   * 플랫폼 정산 주기 계산 방식
   *
   * 하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 정산 주기 계산 방식을 가진 계약만 조회합니다.
   */
  val cycleTypes: List<PlatformSettlementCycleType>? = null,
  /**
   * 플랫폼 정산 기준일
   *
   * 하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 정산 기준일을 가진 계약만 조회합니다.
   */
  val datePolicies: List<PlatformSettlementCycleDatePolicy>? = null,
  /**
   * 보관 조회 여부
   *
   * true 이면 보관된 계약을 조회하고, false 이면 보관되지 않은 계약을 조회합니다. 기본값은 false 입니다.
   */
  val isArchived: Boolean? = null,
  /** 검색 키워드 */
  val keyword: PlatformContractFilterInputKeyword? = null,
)


