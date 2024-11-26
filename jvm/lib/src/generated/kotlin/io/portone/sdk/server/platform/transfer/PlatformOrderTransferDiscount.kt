package io.portone.sdk.server.platform.transfer

import io.portone.sdk.server.platform.PlatformDiscountSharePolicy
import kotlinx.serialization.Serializable

/** 할인 정보 */
@Serializable
public data class PlatformOrderTransferDiscount(
  /** 할인 분담 정책 */
  val sharePolicy: PlatformDiscountSharePolicy,
  /** 할인 금액 */
  val amount: Long,
  /** 면세 할인 금액 */
  val taxFreeAmount: Long,
  /** 할인 분담 금액 */
  val shareAmount: Long,
  /** 면세 할인 분담 금액 */
  val shareTaxFreeAmount: Long,
)


