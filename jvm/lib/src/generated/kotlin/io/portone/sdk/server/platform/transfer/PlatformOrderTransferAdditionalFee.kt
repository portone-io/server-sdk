package io.portone.sdk.server.platform.transfer

import io.portone.sdk.server.platform.PlatformAdditionalFeePolicy
import kotlinx.serialization.Serializable

/** 추가 수수료 정보 */
@Serializable
public data class PlatformOrderTransferAdditionalFee(
  /** 추가 수수료 정책 */
  val policy: PlatformAdditionalFeePolicy,
  /** 추가 수수료 금액 */
  val amount: Long,
  /** 추가 수수료 부가세 금액 */
  val vat: Long,
)


