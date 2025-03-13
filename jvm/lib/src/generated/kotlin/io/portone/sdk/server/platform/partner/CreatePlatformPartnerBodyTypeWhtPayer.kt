package io.portone.sdk.server.platform.partner

import kotlin.String
import kotlinx.serialization.Serializable

@Serializable
public data class CreatePlatformPartnerBodyTypeWhtPayer(
  /**
   * 생년월일
   *
   * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
   * (yyyy-MM-dd)
   */
  val birthdate: String? = null,
)


