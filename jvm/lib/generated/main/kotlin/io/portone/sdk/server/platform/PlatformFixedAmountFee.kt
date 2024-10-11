package io.portone.sdk.server.platform

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/**
 * 정액 수수료
 *
 * 총 금액에 무관하게 정해진 수수료 금액을 책정합니다.
 */
@Serializable
@SerialName("FIXED_AMOUNT")
public data class PlatformFixedAmountFee(
  /** 고정된 수수료 금액 */
  val amount: Long,
): PlatformFee,
