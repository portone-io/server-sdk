package io.portone.sdk.server.platform

import io.portone.sdk.server.platform.PlatformRoundType
import io.portone.sdk.server.platform.UpdatePlatformBodySettlementFormula
import io.portone.sdk.server.platform.UpdatePlatformBodySettlementRule
import kotlinx.serialization.Serializable

/**
 * 플랫폼 업데이트를 위한 입력 정보
 *
 * 값이 명시되지 않은 필드는 업데이트하지 않습니다.
 */
@Serializable
internal data class UpdatePlatformBody(
  /** 파트너 정산금액의 소수점 처리 방식 */
  val roundType: PlatformRoundType? = null,
  /** 수수료 및 할인 분담 정책 관련 계산식 */
  val settlementFormula: UpdatePlatformBodySettlementFormula? = null,
  /** 정산 규칙 */
  val settlementRule: UpdatePlatformBodySettlementRule? = null,
)
