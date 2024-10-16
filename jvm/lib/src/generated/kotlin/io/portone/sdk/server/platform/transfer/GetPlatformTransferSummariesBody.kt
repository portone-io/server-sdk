package io.portone.sdk.server.platform.transfer

import io.portone.sdk.server.common.PageInput
import io.portone.sdk.server.platform.transfer.PlatformTransferFilterInput
import kotlinx.serialization.Serializable

/** 정산건 요약 다건 조회를 위한 입력 정보 */
@Serializable
internal data class GetPlatformTransferSummariesBody(
  /** 요청할 페이지 정보 */
  val page: PageInput? = null,
  /** 조회할 정산건 조건 필터 */
  val filter: PlatformTransferFilterInput? = null,
)
