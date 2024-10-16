package io.portone.sdk.server.platform.policy

import io.portone.sdk.server.common.PageInput
import io.portone.sdk.server.platform.policy.PlatformContractFilterInput
import kotlinx.serialization.Serializable

/** 계약 다건 조회를 위한 입력 정보 */
@Serializable
internal data class GetPlatformContractsBody(
  /** 요청할 페이지 정보 */
  val page: PageInput? = null,
  /** 조회할 계약 조건 필터 */
  val filter: PlatformContractFilterInput? = null,
)
