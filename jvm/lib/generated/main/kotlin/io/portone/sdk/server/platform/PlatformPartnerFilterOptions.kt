package io.portone.sdk.server.platform

import io.portone.sdk.server.platform.PlatformPartnerContractSummary
import kotlin.Array
import kotlin.String
import kotlinx.serialization.Serializable

/** 파트너 필터 옵션 조회 성공 응답 정보 */
@Serializable
public data class PlatformPartnerFilterOptions(
  /** 조회된 태그 리스트 */
  val tags: Array<String>,
  /** 조회된 파트너 계약 요약 정보 리스트 */
  val contractSummary: Array<PlatformPartnerContractSummary>,
)
