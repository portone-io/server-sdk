package io.portone.sdk.server.platform

import kotlinx.serialization.Serializable

/**
 * 수수료 계산 방식을 특정하기 위한 입력 정보
 *
 * 정률 수수료를 설정하고 싶은 경우 `fixedRate` 필드에, 정액 수수료를 설정하고 싶은 경우 `fixedAmount` 필드에 값을 명시해 요청합니다.
 * 두 필드 모두 값이 들어있지 않은 경우 요청이 거절됩니다.
 */
@Serializable
public data class PlatformFeeInput(
  /** 정률 수수료 */
  val fixedRate: Int? = null,
  /** 정액 수수료 */
  val fixedAmount: Long? = null,
)


