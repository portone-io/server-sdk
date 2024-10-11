package io.portone.sdk.server.platform.policy

import io.portone.sdk.server.platform.policy.PlatformDiscountSharePolicyFilterInputKeyword
import kotlin.IntArray
import kotlinx.serialization.Serializable

/** 할인 분담 정책 다건 조회를 위한 필터 조건 */
@Serializable
public data class PlatformDiscountSharePolicyFilterInput(
  /**
   * 보관 조회 여부
   *
   * true 이면 보관된 할인 분담 정책을 조회하고, false 이면 보관되지 않은 할인 분담 정책을 조회합니다. 기본값은 false 입니다.
   */
  val isArchived: Boolean? = null,
  /** 하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 파트너 분담율을 가진 할인 분담 정책만 조회합니다. */
  val partnerShareRates: IntArray? = null,
  /** 검색 키워드 */
  val keyword: PlatformDiscountSharePolicyFilterInputKeyword? = null,
)
