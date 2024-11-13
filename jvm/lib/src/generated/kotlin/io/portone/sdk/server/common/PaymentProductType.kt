package io.portone.sdk.server.common

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 상품 유형 */
@Serializable
public sealed class PaymentProductType {
  /** 실물 상품 */
  @SerialName("PHYSICAL")
  public data object Physical : PaymentProductType()
  /**
   * 디지털 상품
   *
   * 서비스, 온라인 상품 등 실물이 존재하지 않는 무형의 상품을 의미합니다.
   */
  @SerialName("DIGITAL")
  public data object Digital : PaymentProductType()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : PaymentProductType()
}
