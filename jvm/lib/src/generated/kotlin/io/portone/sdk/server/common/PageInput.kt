package io.portone.sdk.server.common

import kotlinx.serialization.Serializable

/** 다건 조회 API 에 사용되는 페이지 입력 정보 */
@Serializable
public data class PageInput(
  /** 0부터 시작하는 페이지 번호 */
  val number: Int? = null,
  /** 각 페이지 당 포함할 객체 수 */
  val size: Int? = null,
)


