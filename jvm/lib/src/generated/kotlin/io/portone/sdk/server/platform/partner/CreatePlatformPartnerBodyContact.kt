package io.portone.sdk.server.platform.partner

import kotlin.String
import kotlinx.serialization.Serializable

/** 파트너 담당자 정보 */
@Serializable
public data class CreatePlatformPartnerBodyContact(
  /** 담당자 이름 */
  val name: String,
  /** 담당자 휴대폰 번호 */
  val phoneNumber: String? = null,
  /** 담당자 이메일 */
  val email: String,
)


