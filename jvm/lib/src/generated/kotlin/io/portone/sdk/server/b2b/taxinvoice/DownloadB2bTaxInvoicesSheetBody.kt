package io.portone.sdk.server.b2b.taxinvoice

import io.portone.sdk.server.b2b.taxinvoice.GetB2bTaxInvoicesBodyFilter
import io.portone.sdk.server.b2b.taxinvoice.TaxInvoicesSheetField
import kotlinx.serialization.Serializable

@Serializable
internal data class DownloadB2bTaxInvoicesSheetBody(
  val filter: GetB2bTaxInvoicesBodyFilter? = null,
  /** 다운로드 할 시트 컬럼 */
  val fields: List<TaxInvoicesSheetField>? = null,
  val test: Boolean? = null,
)


