package io.portone.sdk.server.identityverification

import io.portone.sdk.server.common.Gender
import io.portone.sdk.server.identityverification.IdentityVerificationOperator
import kotlin.String
import kotlinx.serialization.Serializable

/** 인증된 고객 정보 */
@Serializable
public data class IdentityVerificationVerifiedCustomer(
  /** 식별 아이디 */
  val id: String? = null,
  /** 이름 */
  val name: String,
  /**
   * 통신사
   *
   * 다날: 별도 계약이 필요합니다.
   * KG이니시스: 제공하지 않습니다.
   */
  val `operator`: IdentityVerificationOperator? = null,
  /**
   * 전화번호
   *
   * 특수 문자(-) 없이 숫자로만 이루어진 번호 형식입니다.
   * 다날: 별도 계약이 필요합니다.
   * KG이니시스: 항상 제공합니다.
   */
  val phoneNumber: String? = null,
  /**
   * 생년월일 (yyyy-MM-dd)
   *
   * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
   */
  val birthDate: String,
  /**
   * 성별
   *
   * 다날: 항상 제공합니다.
   * KG이니시스: 항상 제공합니다.
   */
  val gender: Gender? = null,
  /**
   * 외국인 여부
   *
   * 다날: 별도 계약이 필요합니다.
   * KG이니시스: 항상 제공합니다.
   */
  val isForeigner: Boolean? = null,
  /**
   * CI (개인 고유 식별키)
   *
   * 개인을 식별하기 위한 고유 정보입니다.
   * 다날: 항상 제공합니다.
   * KG이니시스: 카카오를 제외한 인증사에서 제공합니다.
   */
  val ci: String? = null,
  /**
   * DI (사이트별 개인 고유 식별키)
   *
   * 중복 가입을 방지하기 위해 개인을 식별하는 사이트별 고유 정보입니다.
   * 다날: 항상 제공합니다.
   * KG이니시스: 제공하지 않습니다.
   */
  val di: String? = null,
)


