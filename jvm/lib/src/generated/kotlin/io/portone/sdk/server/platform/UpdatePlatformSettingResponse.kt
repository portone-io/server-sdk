package io.portone.sdk.server.platform

import io.portone.sdk.server.platform.PlatformSetting
import kotlinx.serialization.Serializable

/** 플랫폼 설정 업데이트 결과 */
@Serializable
public data class UpdatePlatformSettingResponse(
  val setting: PlatformSetting,
)


