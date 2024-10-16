package io.portone.sdk.server.platform.policy

import io.portone.sdk.server.common.PageInput
import io.portone.sdk.server.platform.policy.PlatformAdditionalFeePolicyFilterInput
import kotlinx.serialization.Serializable

/** 추가 수수료 정책 다건 조회를 위한 입력 정보 */
@Serializable
internal data class GetPlatformAdditionalFeePoliciesBody(
  /** 요청할 페이지 정보 */
  val page: PageInput? = null,
  /** 조회할 추가 수수료 정책 조건 필터 */
  val filter: PlatformAdditionalFeePolicyFilterInput? = null,
)
