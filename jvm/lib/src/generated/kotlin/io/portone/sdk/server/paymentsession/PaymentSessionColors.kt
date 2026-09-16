package io.portone.sdk.server.paymentsession

import kotlin.String
import kotlinx.serialization.Serializable

/** 체크아웃 페이지 색 설정 */
@Serializable
public data class PaymentSessionColors(
  /**
   * 주 색상
   *
   * CSS 색 문자열 형식
   */
  val primary: String? = null,
  /**
   * 호버 주 색상
   *
   * CSS 색 문자열 형식
   */
  val primaryHover: String? = null,
  /**
   * 밝은 주 색상
   *
   * CSS 색 문자열 형식
   */
  val primaryLight: String? = null,
)


