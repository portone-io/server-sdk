package io.portone.sdk.server.platform

import io.portone.sdk.server.platform.PlatformRoundType
import io.portone.sdk.server.platform.PlatformSettlementFormula
import io.portone.sdk.server.platform.PlatformSettlementRule
import kotlin.String
import kotlinx.serialization.Serializable

/** 고객사의 플랫폼 기능 관련 정보 */
@Serializable
public data class Platform(
  /** 해당 플랫폼의 고객사 아이디 */
  val merchantId: String,
  val graphqlId: String,
  /** 파트너 정산금액의 소수점 처리 방식 */
  val roundType: PlatformRoundType,
  /** 수수료 및 할인 분담 정책 관련 계산식 */
  val settlementFormula: PlatformSettlementFormula,
  /** 정산 규칙 */
  val settlementRule: PlatformSettlementRule,
)


