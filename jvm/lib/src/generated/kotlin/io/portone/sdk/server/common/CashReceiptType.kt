package io.portone.sdk.server.common

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 발급 유형 */
@Serializable
public sealed interface CashReceiptType {
  public val value: String
  /** 소득공제용 */
  @SerialName("PERSONAL")
  public data object Personal : CashReceiptType {
    override val value: String = "PERSONAL"
  }
  /** 지출증빙용 */
  @SerialName("CORPORATE")
  public data object Corporate : CashReceiptType {
    override val value: String = "CORPORATE"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : CashReceiptType
}
