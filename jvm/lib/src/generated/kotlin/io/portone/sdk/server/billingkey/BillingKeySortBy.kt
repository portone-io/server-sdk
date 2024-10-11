package io.portone.sdk.server.billingkey

import kotlinx.serialization.Serializable

/** 빌링키 정렬 기준 */
@Serializable
public enum class BillingKeySortBy {
  /** 발급 요청 시각 */
  REQUESTED_AT,
  /** 발급 완료 시각 */
  ISSUED_AT,
  /** 삭제 완료 시각 */
  DELETED_AT,
  /**
   * 상태 변경 시각
   *
   * 발급 완료 상태의 경우 ISSUED_AT, 삭제 완료 상태의 경우 DELETED_AT
   */
  STATUS_TIMESTAMP,
}
