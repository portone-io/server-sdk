package io.portone.sdk.server.platform.accounttransfer

import io.portone.sdk.server.common.PageInput
import io.portone.sdk.server.platform.accounttransfer.PlatformAccountTransferFilter
import kotlinx.serialization.Serializable

@Serializable
public data class GetAccountTransfersBody(
  val isForTest: Boolean? = null,
  val page: PageInput? = null,
  val filter: PlatformAccountTransferFilter? = null,
)
