package io.portone.sdk.server.platform.transfer

import kotlin.String
import kotlinx.serialization.Serializable

/** 할인 정보 */
@Serializable
public data class CreatePlatformOrderTransferBodyDiscount(
  /** 할인 분담 정책 아이디 */
  val sharePolicyId: String,
  /** 할인 금액 */
  val amount: Long,
  /** 면세 할인 금액 */
  val taxFreeAmount: Long? = null,
)
