package io.portone.sdk.server.platform.transfer

import kotlinx.serialization.Serializable

/** 간편 결제 수단 */
@Serializable
public enum class EasyPayMethodType {
  CARD,
  TRANSFER,
  CHARGE,
}
