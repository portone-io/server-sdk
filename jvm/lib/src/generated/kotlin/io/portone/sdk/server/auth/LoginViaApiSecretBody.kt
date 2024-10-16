package io.portone.sdk.server.auth

import kotlin.String
import kotlinx.serialization.Serializable

/** API Secret 로그인을 위한 입력 정보 */
@Serializable
internal data class LoginViaApiSecretBody(
  /** 발급받은 API secret */
  val apiSecret: String,
)
