package io.portone.sdk.server.identityverification

import io.portone.sdk.server.common.PageInput
import io.portone.sdk.server.identityverification.IdentityVerificationFilterInput
import io.portone.sdk.server.identityverification.IdentityVerificationSortInput
import kotlinx.serialization.Serializable

/** 본인인증 내역 다건 조회를 위한 입력 정보 */
@Serializable
internal data class GetIdentityVerificationsBody(
  /**
   * 요청할 페이지 정보
   *
   * 미 입력 시 number: 0, size: 10 으로 기본값이 적용됩니다.
   */
  val page: PageInput? = null,
  /**
   * 정렬 조건
   *
   * 미 입력 시 sortBy: REQUESTED_AT, sortOrder: DESC 으로 기본값이 적용됩니다.
   */
  val sort: IdentityVerificationSortInput? = null,
  /** 조회할 본인인증 내역 조건 필터 */
  val filter: IdentityVerificationFilterInput? = null,
)


