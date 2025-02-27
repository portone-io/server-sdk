package io.portone.sdk.server.identityverification

import io.portone.sdk.server.common.SortOrder
import io.portone.sdk.server.identityverification.IdentityVerificationSortBy
import kotlinx.serialization.Serializable

/** 본인인증 내역 다건 조회 시 정렬 조건 */
@Serializable
public data class IdentityVerificationSortInput(
  /**
   * 정렬 기준 필드
   *
   * 어떤 필드를 기준으로 정렬할 지 결정합니다. 비워서 보낼 경우, REQUESTED_AT이 기본값으로 설정됩니다.
   */
  val by: IdentityVerificationSortBy? = null,
  /**
   * 정렬 순서
   *
   * 어떤 순서로 정렬할 지 결정합니다. 비워서 보낼 경우, DESC(내림차순)가 기본값으로 설정됩니다.
   */
  val order: SortOrder? = null,
)


