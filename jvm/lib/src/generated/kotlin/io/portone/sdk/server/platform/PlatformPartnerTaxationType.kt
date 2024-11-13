package io.portone.sdk.server.platform

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 플랫폼 파트너 과세 유형 */
@Serializable
public sealed class PlatformPartnerTaxationType {
  /** 일반 과세 */
  @SerialName("NORMAL")
  public data object Normal : PlatformPartnerTaxationType()
  /** 간이과세(세금계산서 발행) */
  @SerialName("SIMPLE_TAX_INVOICE_ISSUER")
  public data object SimpleTaxInvoiceIssuer : PlatformPartnerTaxationType()
  /** 간이과세(세금계산서 미발행) */
  @SerialName("SIMPLE")
  public data object Simple : PlatformPartnerTaxationType()
  /** 면세 */
  @SerialName("TAX_FREE")
  public data object TaxFree : PlatformPartnerTaxationType()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : PlatformPartnerTaxationType()
}
