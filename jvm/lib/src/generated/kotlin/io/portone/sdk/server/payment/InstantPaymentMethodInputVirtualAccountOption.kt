package io.portone.sdk.server.payment

import io.portone.sdk.server.payment.InstantPaymentMethodInputVirtualAccountOptionFixed
import io.portone.sdk.server.payment.InstantPaymentMethodInputVirtualAccountOptionType
import kotlinx.serialization.Serializable

/** 가상계좌 발급 방식 */
@Serializable
public data class InstantPaymentMethodInputVirtualAccountOption(
  /** 발급 유형 */
  val type: InstantPaymentMethodInputVirtualAccountOptionType,
  /**
   * 고정식 가상계좌 발급 방식
   *
   * 발급 유형을 FIXED 로 선택했을 시에만 입력합니다.
   */
  val fixed: InstantPaymentMethodInputVirtualAccountOptionFixed? = null,
)


