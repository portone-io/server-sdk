package io.portone.sdk.server.billingkey

import io.portone.sdk.server.billingkey.BillingKeyInfo
import io.portone.sdk.server.common.PageInfo
import kotlinx.serialization.Serializable

/** 빌링키 다건 조회 성공 응답 정보 */
@Serializable
public data class GetBillingKeyInfosResponse(
  /** 조회된 빌링키 리스트 */
  val items: List<BillingKeyInfo>,
  /** 조회된 페이지 정보 */
  val page: PageInfo,
)
