package io.portone.sdk.server.platform

import kotlin.String
import kotlinx.serialization.Serializable

/** 플랫폼 내 발생하는 여러 수수료 및 할인 분담에 관한 계산식 정보 */
@Serializable
public data class PlatformSettlementFormula(
  /** 플랫폼 수수료 계산식 */
  val platformFee: String,
  /** 할인 분담액 계산식 */
  val discountShare: String,
  /** 추가 수수료 계산식 */
  val additionalFee: String,
)


