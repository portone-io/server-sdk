package io.portone.sdk.server.platform.transfer

import kotlinx.serialization.Serializable

/** 플랫폼 정산 파라미터 값 */
@Serializable
public data class PlatformSettlementParameterValue(
  /** 크기가 조정되지 않은 숫자 */
  val decimal: Long,
  /**
   * 소수 자리수
   *
   * 정산 시 필요한 `decimalScale`이 지정되지 않은 경우 기본값으로 0을 사용합니다.
   * 입력 가능한 법위는 0 ~ 5 입니다.
   */
  val decimalScale: Int? = null,
)
