package io.portone.sdk.server.common

import kotlinx.serialization.Serializable

/** 반환된 페이지 결과 정보 */
@Serializable
public data class PageInfo(
  /** 요청된 페이지 번호 */
  val number: Int,
  /** 요청된 페이지 당 객체 수 */
  val size: Int,
  /** 실제 반환된 객체 수 */
  val totalCount: Int,
)
