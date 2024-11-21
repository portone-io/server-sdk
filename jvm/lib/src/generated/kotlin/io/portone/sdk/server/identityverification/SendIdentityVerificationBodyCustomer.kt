package io.portone.sdk.server.identityverification

import kotlin.String
import kotlinx.serialization.Serializable

/** 본인인증 요청을 위한 고객 정보 */
@Serializable
public data class SendIdentityVerificationBodyCustomer(
  /** 식별 아이디 */
  val id: String? = null,
  /** 이름 */
  val name: String,
  /**
   * 전화번호
   *
   * 특수 문자(-) 없이 숫자만 입력합니다.
   */
  val phoneNumber: String,
  /**
   * 주민등록번호 앞 7자리
   *
   * SMS 방식의 경우 필수로 입력합니다.
   */
  val identityNumber: String? = null,
  /**
   * IP 주소
   *
   * 고객의 요청 속도 제한에 사용됩니다.
   */
  val ipAddress: String,
)
