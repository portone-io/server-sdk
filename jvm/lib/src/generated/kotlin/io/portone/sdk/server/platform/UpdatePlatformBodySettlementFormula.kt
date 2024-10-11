package io.portone.sdk.server.platform

import kotlin.String
import kotlinx.serialization.Serializable

/**
 * 플랫폼 업데이트 시 변경할 계산식 정보
 *
 * 값이 명시되지 않은 필드는 업데이트하지 않습니다.
 */
@Serializable
public data class UpdatePlatformBodySettlementFormula(
  /** 플랫폼 수수료 계산식 */
  val platformFee: String? = null,
  /** 할인 분담액 계산식 */
  val discountShare: String? = null,
  /** 추가 수수료 계산식 */
  val additionalFee: String? = null,
)
