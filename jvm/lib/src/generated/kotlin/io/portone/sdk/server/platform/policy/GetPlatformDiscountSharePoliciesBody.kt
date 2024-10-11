package io.portone.sdk.server.platform.policy

import io.portone.sdk.server.common.PageInput
import io.portone.sdk.server.platform.policy.PlatformDiscountSharePolicyFilterInput
import kotlinx.serialization.Serializable

/** 할인 분담 정책 다건 조회를 위한 입력 정보 */
@Serializable
public data class GetPlatformDiscountSharePoliciesBody(
  /** 요청할 페이지 정보 */
  val page: PageInput? = null,
  /** 조회할 할인 분담 정책 조건 필터 */
  val filter: PlatformDiscountSharePolicyFilterInput? = null,
)
