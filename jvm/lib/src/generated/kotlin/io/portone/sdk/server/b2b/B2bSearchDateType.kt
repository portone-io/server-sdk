package io.portone.sdk.server.b2b

import kotlinx.serialization.Serializable

/** 조회 기준 */
@Serializable
public enum class B2bSearchDateType {
  /** 등록일 */
  REGISTER,
  /** 작성일 */
  WRITE,
  /** 발행일 */
  ISSUE,
}
