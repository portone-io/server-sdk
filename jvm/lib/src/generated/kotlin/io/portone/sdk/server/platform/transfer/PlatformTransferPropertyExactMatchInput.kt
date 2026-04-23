package io.portone.sdk.server.platform.transfer

import kotlin.String
import kotlinx.serialization.Serializable

/** 사용자 정의 속성 key/value exact match */
@Serializable
public data class PlatformTransferPropertyExactMatchInput(
  /** 키 */
  val key: String,
  /** 값 */
  val value: String,
)


