package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.DeleteB2bTaxInvoiceError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/**
 * 세금계산서가 삭제 가능한 상태가 아닌 경우
 *
 * 삭제 가능한 상태는 `REGISTERED`, `ISSUE_REFUSED`, `REQUEST_CANCELLED_BY_RECIPIENT`, `ISSUE_CANCELLED_BY_SUPPLIER`, `SENDING_FAILED` 입니다.
 */
@Serializable
@SerialName("B2B_TAX_INVOICE_NON_DELETABLE_STATUS")
@ConsistentCopyVisibility
public data class B2bTaxInvoiceNonDeletableStatusError internal constructor(
  val message: String? = null,
): DeleteB2bTaxInvoiceError
