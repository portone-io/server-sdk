package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.DraftB2bTaxInvoiceError
import io.portone.sdk.server.errors.RequestB2bTaxInvoiceReverseIssuanceError
import io.portone.sdk.server.errors.UpdateB2bTaxInvoiceDraftError
import io.portone.sdk.server.errors.requestB2bTaxInvoiceError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 세금계산서 과세 유형을 수정할 수 없는 경우 */
@Serializable
@SerialName("B2B_CANNOT_CHANGE_TAX_TYPE")
@ConsistentCopyVisibility
public data class B2BCannotChangeTaxTypeError internal constructor(
  override val message: String? = null,
): DraftB2bTaxInvoiceError,
  RequestB2bTaxInvoiceReverseIssuanceError,
  UpdateB2bTaxInvoiceDraftError,
  requestB2bTaxInvoiceError
