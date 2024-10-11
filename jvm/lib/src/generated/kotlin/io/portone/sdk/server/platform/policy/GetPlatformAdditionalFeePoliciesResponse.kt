package io.portone.sdk.server.platform.policy

import io.portone.sdk.server.common.PageInfo
import io.portone.sdk.server.platform.PlatformAdditionalFeePolicy
import kotlinx.serialization.Serializable

/** 추가 수수료 정책 다건 조회 성공 응답 정보 */
@Serializable
public data class GetPlatformAdditionalFeePoliciesResponse(
  /** 조회된 추가 수수료 정책 리스트 */
  val items: List<PlatformAdditionalFeePolicy>,
  /** 조회된 페이지 정보 */
  val page: PageInfo,
)
