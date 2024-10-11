package io.portone.sdk.server.common

import kotlin.String
import kotlinx.serialization.Serializable

/** 카드 인증 관련 정보 */
@Serializable
public data class CardCredential(
  /** 카드 번호 (숫자만) */
  val number: String,
  /** 유효 기간 만료 연도 (2자리) */
  val expiryYear: String,
  /** 유효 기간 만료 월 (2자리) */
  val expiryMonth: String,
  /** 생년월일 (yyMMdd) 또는 사업자 등록 번호 (10자리, 숫자만) */
  val birthOrBusinessRegistrationNumber: String? = null,
  /** 비밀번호 앞 2자리 */
  val passwordTwoDigits: String? = null,
)
