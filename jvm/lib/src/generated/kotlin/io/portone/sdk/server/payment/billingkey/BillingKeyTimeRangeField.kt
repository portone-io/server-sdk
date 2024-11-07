package io.portone.sdk.server.payment.billingkey

import kotlinx.serialization.Serializable

/** 빌링키 다건 조회 시, 시각 범위를 적용할 필드 */
@Serializable
public enum class BillingKeyTimeRangeField {
  /** 발급 요청 시각 */
  RequestedAt,
  /** 발급 완료 시각 */
  IssuedAt,
  /** 삭제 완료 시각 */
  DeletedAt,
  /**
   * 상태 변경 시각
   *
   * 발급 완료 상태의 경우 ISSUED_AT, 삭제 완료 상태의 경우 DELETED_AT
   */
  StatusTimestamp,
}
