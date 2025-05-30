package io.portone.sdk.server.platform.company

import io.portone.sdk.server.platform.company.B2bBusinessInfoResult
import kotlinx.serialization.Serializable

/** 사업자등록 정보 조회 성공 응답 */
@Serializable
public data class GetB2bBusinessInfosResponse(
  /** 사업자등록 정보 리스트 */
  val result: List<B2bBusinessInfoResult>,
)


