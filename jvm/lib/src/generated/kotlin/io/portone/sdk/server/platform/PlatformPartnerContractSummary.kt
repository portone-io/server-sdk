package io.portone.sdk.server.platform

import kotlin.String
import kotlinx.serialization.Serializable

/** 파트너 계약 요약 정보 */
@Serializable
public data class PlatformPartnerContractSummary(
  /** 계약 고유 아이디 */
  val id: String,
  /** 계약 이름 */
  val name: String,
)


