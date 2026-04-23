package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 거래처가 존재하지 않는 경우 */
@Serializable
@SerialName("B2B_COUNTERPARTY_NOT_FOUND")
internal data class B2bCounterpartyNotFoundError(
  override val message: String? = null,
  val counterpartyId: String? = null,
) : DeleteB2bCounterpartyError.Recognized, DraftB2bTaxInvoiceError.Recognized, GetB2bCounterpartyCertificateError.Recognized, GetB2bCounterpartyCertificateRegistrationUrlError.Recognized, GetB2bCounterpartyError.Recognized, IssueB2bTaxInvoiceImmediatelyError.Recognized, RequestB2bTaxInvoiceReverseIssuanceError.Recognized, UpdateB2bCounterpartyError.Recognized, UpdateB2bTaxInvoiceDraftError.Recognized, ValidateB2bCounterpartyCertificateError.Recognized


