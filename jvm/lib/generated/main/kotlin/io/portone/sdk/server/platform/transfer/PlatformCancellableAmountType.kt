package io.portone.sdk.server.platform.transfer

import kotlinx.serialization.Serializable

/** 금액 타입 */
@Serializable
public enum class PlatformCancellableAmountType {
  /**
   * 공급대가
   *
   * 공급가액과 부가세를 더한 금액입니다.
   */
  SUPPLY_WITH_VAT,
  /** 면세 금액 */
  TAX_FREE,
}
