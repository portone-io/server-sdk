package io.portone.sdk.server.b2b.business

import io.portone.sdk.server.b2b.business.B2bBusinessInfoResult
import kotlinx.serialization.Serializable

/** 사업자 정보 다건 조회 성공 응답 */
@Serializable
public data class GetB2bBusinessInfosResponse(
  /** 사업자 정보 다건 조회 결과 리스트 */
  val result: List<B2bBusinessInfoResult>,
)


