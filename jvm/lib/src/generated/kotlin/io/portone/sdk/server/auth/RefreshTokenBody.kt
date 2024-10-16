package io.portone.sdk.server.auth

import kotlin.String
import kotlinx.serialization.Serializable

/** 토큰 재발급을 위한 입력 정보 */
@Serializable
internal data class RefreshTokenBody(
  /** 리프레시 토큰 */
  val refreshToken: String,
)
