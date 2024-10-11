package io.portone.sdk.server.b2b

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 공급받는자가 존재하지 않은 경우 */
@Serializable
@SerialName("B2B_RECIPIENT_NOT_FOUND")
public data class B2bRecipientNotFoundError(
  override val message: String? = null,
): RequestB2bTaxInvoiceRegisterError,
  ): RequestB2bTaxInvoiceReverseIssuanceError,
