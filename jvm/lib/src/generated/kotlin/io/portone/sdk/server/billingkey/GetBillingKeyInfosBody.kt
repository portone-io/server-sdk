package io.portone.sdk.server.billingkey

import io.portone.sdk.server.billingkey.BillingKeyFilterInput
import io.portone.sdk.server.billingkey.BillingKeySortInput
import io.portone.sdk.server.common.PageInput
import kotlinx.serialization.Serializable

/** 빌링키 다건 조회를 위한 입력 정보 */
@Serializable
public data class GetBillingKeyInfosBody(
  /**
   * 요청할 페이지 정보
   *
   * 미 입력 시 number: 0, size: 10 으로 기본값이 적용됩니다.
   */
  val page: PageInput? = null,
  /**
   * 정렬 조건
   *
   * 미 입력 시 sortBy: TIME_TO_PAY, sortOrder: DESC 으로 기본값이 적용됩니다.
   */
  val sort: BillingKeySortInput? = null,
  /**
   * 조회할 빌링키 조건 필터
   *
   * V1 빌링키 건의 경우 일부 필드에 대해 필터가 적용되지 않을 수 있습니다.
   */
  val filter: BillingKeyFilterInput? = null,
)
