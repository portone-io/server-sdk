package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.RequestB2bTaxInvoiceRegisterError
import io.portone.sdk.server.errors.RequestB2bTaxInvoiceReverseIssuanceError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 공급자가 존재하지 않은 경우 */
@Serializable
@SerialName("B2B_SUPPLIER_NOT_FOUND")
@ConsistentCopyVisibility
public data class B2bSupplierNotFoundError internal constructor(
  val message: String? = null,
): RequestB2bTaxInvoiceRegisterError,
  RequestB2bTaxInvoiceReverseIssuanceError
