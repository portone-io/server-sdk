package io.portone.sdk.server.platform.policy

import io.portone.sdk.server.common.PageInfo
import io.portone.sdk.server.platform.PlatformContract
import kotlinx.serialization.Serializable

/** 계약 다건 조회 성공 응답 */
@Serializable
public data class GetPlatformContractsResponse(
  /** 조회된 계약 리스트 */
  val items: Array<PlatformContract>,
  /** 조회된 페이지 정보 */
  val page: PageInfo,
)
