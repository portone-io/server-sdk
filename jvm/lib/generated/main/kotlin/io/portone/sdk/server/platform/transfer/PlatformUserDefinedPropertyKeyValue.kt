package io.portone.sdk.server.platform.transfer

import io.portone.sdk.server.platform.PlatformUserDefinedPropertyValue
import kotlin.String
import kotlinx.serialization.Serializable

/** 사용자 정의 속성 */
@Serializable
public data class PlatformUserDefinedPropertyKeyValue(
  /** 사용자 정의 속성 키 */
  val key: String,
  /** 사용자 정의 속성 값 */
  val value: PlatformUserDefinedPropertyValue,
)
