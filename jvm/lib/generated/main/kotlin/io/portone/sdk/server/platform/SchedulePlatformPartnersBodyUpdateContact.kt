package io.portone.sdk.server.platform

import kotlin.String
import kotlinx.serialization.Serializable

/** 파트너 업데이트를 위한 유형별 추가 정보 */
@Serializable
public data class SchedulePlatformPartnersBodyUpdateContact(
  /** 담당자 이름 */
  val name: String? = null,
  /** 담당자 휴대폰 번호 */
  val phoneNumber: String? = null,
  /** 담당자 이메일 */
  val email: String? = null,
)
