package io.portone.sdk.server.common

import io.portone.sdk.server.common.Address
import io.portone.sdk.server.common.Gender
import kotlin.String
import kotlinx.serialization.Serializable

/** 고객 정보 */
@Serializable
public data class Customer(
  /**
   * 고객 아이디
   *
   * 고객사가 지정한 고객의 고유 식별자입니다.
   */
  val id: String? = null,
  /** 이름 */
  val name: String? = null,
  /** 출생 연도 */
  val birthYear: String? = null,
  /** 성별 */
  val gender: Gender? = null,
  /** 이메일 */
  val email: String? = null,
  /** 전화번호 */
  val phoneNumber: String? = null,
  /** 주소 */
  val address: Address? = null,
  /** 우편번호 */
  val zipcode: String? = null,
)


