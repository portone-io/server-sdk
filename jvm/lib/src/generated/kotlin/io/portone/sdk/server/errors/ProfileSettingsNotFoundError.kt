package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 프로필 설정이 존재하지 않는 경우 */
@Serializable
@SerialName("PROFILE_SETTINGS_NOT_FOUND")
internal data class ProfileSettingsNotFoundError(
  override val message: String? = null,
) : EvaluateCheckoutProfileError.Recognized


