package io.portone.sdk.server.platform.transfer

import io.portone.sdk.server.common.EasyPayProvider
import io.portone.sdk.server.platform.transfer.EasyPayMethodType
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 간편 결제 */
@Serializable
@SerialName("EASY_PAY")
public data class PlatformPaymentMethodEasyPay(
  /** 간편 결제사 */
  val provider: EasyPayProvider? = null,
  /** 간편 결제 수단 */
  val methodType: EasyPayMethodType? = null,
): PlatformPaymentMethod,
