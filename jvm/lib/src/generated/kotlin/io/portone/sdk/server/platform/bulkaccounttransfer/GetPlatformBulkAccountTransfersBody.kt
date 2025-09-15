package io.portone.sdk.server.platform.bulkaccounttransfer

import io.portone.sdk.server.common.PageInput
import io.portone.sdk.server.platform.bulkaccounttransfer.PlatformBulkAccountTransferFilterInput
import kotlinx.serialization.Serializable

@Serializable
internal data class GetPlatformBulkAccountTransfersBody(
  val isForTest: Boolean? = null,
  val page: PageInput? = null,
  val filter: PlatformBulkAccountTransferFilterInput? = null,
)


