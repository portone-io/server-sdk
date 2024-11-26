package io.portone.sdk.server.platform.transfer

import io.portone.sdk.server.common.PageInfo
import io.portone.sdk.server.platform.transfer.PlatformTransferSummary
import kotlinx.serialization.Serializable

@Serializable
public data class GetPlatformTransferSummariesResponse(
  val transferSummaries: List<PlatformTransferSummary>,
  val page: PageInfo,
)


