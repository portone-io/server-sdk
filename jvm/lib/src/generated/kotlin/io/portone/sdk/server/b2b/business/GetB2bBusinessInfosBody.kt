package io.portone.sdk.server.b2b.business

import kotlin.Array
import kotlin.String
import kotlinx.serialization.Serializable

/** 사업자 정보 다건 조회를 위한 입력 정보 */
@Serializable
internal data class GetB2bBusinessInfosBody(
  /** 조회할 사업자등록번호 리스트 */
  val brnList: List<String>,
)


