package io.portone.sdk.server.platform.accounttransfer

import io.portone.sdk.server.common.PageInput
import io.portone.sdk.server.platform.accounttransfer.PlatformAccountTransferFilter
import kotlinx.serialization.Serializable

@Serializable
internal data class GetAccountTransfersBody1(
  val isForTest: Boolean? = null,
  val page: PageInput? = null,
  val filter: PlatformAccountTransferFilter? = null,
)


