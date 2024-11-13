package io.portone.sdk.server.common

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 발급 유형 */
@Serializable
public sealed class CashReceiptType {
  /** 소득공제용 */
  @SerialName("PERSONAL")
  public data object Personal : CashReceiptType()
  /** 지출증빙용 */
  @SerialName("CORPORATE")
  public data object Corporate : CashReceiptType()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : CashReceiptType()
}
