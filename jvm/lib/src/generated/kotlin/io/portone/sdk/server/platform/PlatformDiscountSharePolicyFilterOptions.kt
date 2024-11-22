package io.portone.sdk.server.platform

import kotlin.IntArray
import kotlinx.serialization.Serializable

/** 할인 분담 정책 필터 옵션 조회 성공 응답 정보 */
@Serializable
public data class PlatformDiscountSharePolicyFilterOptions(
  /** 조회된 파트너 분담율 리스트 */
  val partnerShareRates: IntArray,
)


