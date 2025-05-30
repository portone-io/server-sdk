package io.portone.sdk.server.platform

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/**
 * 원천징수 비대상자 파트너 정보
 *
 * 비사업자 유형의 파트너 추가 정보 입니다.
 */
@Serializable
@SerialName("NON_WHT_PAYER")
public data class PlatformPartnerTypeNonWhtPayer(
  /**
   * 생년월일
   *
   * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
   * (yyyy-MM-dd)
   */
  val birthdate: String? = null,
) : PlatformPartnerType.Recognized


