package io.portone.sdk.server.auth

import kotlin.String
import kotlinx.serialization.Serializable

/** API key 로그인 성공 응답 */
@Serializable
public data class LoginViaApiSecretResponse(
  /**
   * 인증에 사용하는 엑세스 토큰
   *
   * 하루의 유효기간을 가지고 있습니다.
   */
  val accessToken: String,
  /**
   * 토큰 재발급 및 유효기간 연장을 위해 사용하는 리프레시 토큰
   *
   * 일주일의 유효기간을 가지고 있으며, 리프레시 토큰을 통해 유효기간이 연장된 새로운 엑세스 토큰을 발급받을 수 있습니다.
   * 동일한 유저가 로그인 또는 토큰 재발급을 진행할 때마다 기존에 발급된 리프레시 토큰은 즉시 만료되므로 API 사용에 유의해주세요.
   */
  val refreshToken: String,
)
