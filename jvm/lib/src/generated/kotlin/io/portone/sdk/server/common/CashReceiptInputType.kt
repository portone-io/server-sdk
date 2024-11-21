package io.portone.sdk.server.common

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 입력 시 발급 유형 */
@Serializable
public sealed interface CashReceiptInputType {
  public val value: String
  /** 소득공제용 */
  @SerialName("PERSONAL")
  public data object Personal : CashReceiptInputType {
    override val value: String = "PERSONAL"
  }
  /** 지출증빙용 */
  @SerialName("CORPORATE")
  public data object Corporate : CashReceiptInputType {
    override val value: String = "CORPORATE"
  }
  /**
   * 미발행
   *
   * PG사 설정에 따라 PG사가 자동으로 자진발급 처리할 수 있습니다.
   */
  @SerialName("NO_RECEIPT")
  public data object NoReceipt : CashReceiptInputType {
    override val value: String = "NO_RECEIPT"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : CashReceiptInputType
}
