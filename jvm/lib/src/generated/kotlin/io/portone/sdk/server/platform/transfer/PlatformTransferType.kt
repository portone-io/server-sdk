package io.portone.sdk.server.platform.transfer

import kotlinx.serialization.Serializable

@Serializable
public enum class PlatformTransferType {
  ORDER,
  ORDER_CANCEL,
  MANUAL,
}
