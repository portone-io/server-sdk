package io.portone.sdk.server.payment

import kotlinx.serialization.Serializable

/** 가상계좌 유형 */
@Serializable
public enum class PaymentMethodVirtualAccountType {
  /** 고정식 */
  FIXED,
  /** 회전식 */
  NORMAL,
}
