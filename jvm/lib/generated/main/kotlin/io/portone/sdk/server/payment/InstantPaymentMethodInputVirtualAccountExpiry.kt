package io.portone.sdk.server.payment

import kotlinx.datetime.Instant
import kotlinx.serialization.Serializable

/**
 * 입금 만료 기한
 *
 * validHours와 dueDate 둘 중 하나의 필드만 입력합니다.
 */
@Serializable
public data class InstantPaymentMethodInputVirtualAccountExpiry(
  /**
   * 유효 시간
   *
   * 시간 단위로 입력합니다.
   */
  val validHours: Int? = null,
  /** 만료 시점 */
  val dueDate: Instant? = null,
)
