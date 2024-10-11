package io.portone.sdk.server.platform.transfer

import io.portone.sdk.server.common.EasyPayProvider
import io.portone.sdk.server.platform.transfer.EasyPayMethodType
import kotlinx.serialization.Serializable

/** 간편 결제 입력 정보 */
@Serializable
public data class PlatformPaymentMethodEasyPayInput(
  /** 간편 결제사 */
  val provider: EasyPayProvider? = null,
  /** 간편 결제 수단 */
  val methodType: EasyPayMethodType? = null,
)
