package io.portone.sdk.server.platform.bulkaccounttransfer

import io.portone.sdk.server.common.PageInput
import io.portone.sdk.server.platform.bulkaccounttransfer.PlatformBulkAccountTransferFilterInput
import kotlinx.serialization.Serializable

@Serializable
internal data class GetPlatformBulkAccountTransfersBody(
  /**
   * Query Parameter의 test에 값이 제공된 경우 Query Parameter의 test를 사용하고 해당 값은 무시됩니다.
   * Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
   */
  val isForTest: Boolean? = null,
  val page: PageInput? = null,
  val filter: PlatformBulkAccountTransferFilterInput? = null,
)


