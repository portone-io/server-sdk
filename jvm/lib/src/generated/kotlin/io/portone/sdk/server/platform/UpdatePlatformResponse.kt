package io.portone.sdk.server.platform

import io.portone.sdk.server.platform.Platform
import kotlinx.serialization.Serializable

/** 플랫폼 업데이트 결과 정보 */
@Serializable
public data class UpdatePlatformResponse(
  /** 업데이트된 플랫폼 정보 */
  val platform: Platform,
)


