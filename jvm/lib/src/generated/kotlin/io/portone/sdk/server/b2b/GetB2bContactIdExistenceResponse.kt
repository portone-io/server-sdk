package io.portone.sdk.server.b2b

import kotlinx.serialization.Serializable

/** 담당자 ID 존재 여부 응답 정보 */
@Serializable
public data class GetB2bContactIdExistenceResponse(
  /** 존재 여부 */
  val exists: Boolean,
)
