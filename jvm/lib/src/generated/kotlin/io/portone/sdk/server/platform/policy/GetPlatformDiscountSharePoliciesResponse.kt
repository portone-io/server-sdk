package io.portone.sdk.server.platform.policy

import io.portone.sdk.server.common.PageInfo
import io.portone.sdk.server.platform.PlatformDiscountSharePolicy
import kotlinx.serialization.Serializable

/** 할인 분담 정책 다건 조회 성공 응답 정보 */
@Serializable
public data class GetPlatformDiscountSharePoliciesResponse(
  /** 조회된 할인 분담 정책 리스트 */
  val items: List<PlatformDiscountSharePolicy>,
  /** 조회된 페이지 정보 */
  val page: PageInfo,
)


