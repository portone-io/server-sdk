package io.portone.sdk.server.platform

import kotlin.String
import kotlinx.serialization.Serializable

/**
 * 플랫폼 파트너 담당자 연락 정보
 *
 * 파트너 담당자에게 연락하기 위한 정보들 입니다.
 */
@Serializable
public data class PlatformContact(
  /** 담당자 이름 */
  val name: String,
  /** 담당자 휴대폰 번호 */
  val phoneNumber: String? = null,
  /** 담당자 이메일 */
  val email: String,
)
