package io.portone.sdk.server.platform

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 플랫폼 파트너 과세 유형 */
@Serializable
public sealed interface PlatformPartnerTaxationType {
  public val value: String
  /** 일반 과세 */
  @SerialName("NORMAL")
  public data object Normal : PlatformPartnerTaxationType {
    override val value: String = "NORMAL"
  }
  /** 간이과세(세금계산서 발행) */
  @SerialName("SIMPLE_TAX_INVOICE_ISSUER")
  public data object SimpleTaxInvoiceIssuer : PlatformPartnerTaxationType {
    override val value: String = "SIMPLE_TAX_INVOICE_ISSUER"
  }
  /** 간이과세(세금계산서 미발행) */
  @SerialName("SIMPLE")
  public data object Simple : PlatformPartnerTaxationType {
    override val value: String = "SIMPLE"
  }
  /** 면세 */
  @SerialName("TAX_FREE")
  public data object TaxFree : PlatformPartnerTaxationType {
    override val value: String = "TAX_FREE"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformPartnerTaxationType
}
