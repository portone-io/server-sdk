package io.portone.sdk.server.platform.accounttransfer

import io.portone.sdk.server.platform.accounttransfer.PlatformAccountTransferType
import kotlinx.serialization.Serializable

@Serializable
public data class PlatformAccountTransferFilter(
  /** 계좌 이체 유형 */
  val types: Array<PlatformAccountTransferType>? = null,
)
