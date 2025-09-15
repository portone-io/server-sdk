package io.portone.sdk.server.b2b.taxinvoice

import kotlinx.serialization.Serializable

/** BigDecimal 타입 */
@Serializable
public data class Decimal(
  /**
   * 비정규화된 값
   *
   * 소수점 숫자의 비정규화된(unscaled) 값을 정수로 저장합니다. 예를 들어, 123.45의 경우 12345가 저장됩니다.
   */
  val value: Long,
  /**
   * 소수점 이하 자릿수
   *
   * 소수점 숫자의 소수점 이하 자릿수를 저장합니다. 기본값은 0입니다. 예를 들어, 123.45의 경우 2가 저장됩니다.
   */
  val scale: Int? = null,
)


