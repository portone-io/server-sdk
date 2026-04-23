package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 국세청에 연동되어 있지 않은 경우 */
@Serializable
@SerialName("B2B_COUNTERPARTY_NTS_NOT_CONNECTED")
internal data class B2bCounterpartyNtsNotConnectedError(
  override val message: String? = null,
  val brn: String? = null,
  val counterpartyId: String? = null,
) : DraftB2bTaxInvoiceError.Recognized, GetB2bCounterpartyCertificateError.Recognized, GetB2bCounterpartyCertificateRegistrationUrlError.Recognized, IssueB2bTaxInvoiceImmediatelyError.Recognized, RequestB2bTaxInvoiceReverseIssuanceError.Recognized, UpdateB2bTaxInvoiceDraftError.Recognized, ValidateB2bCounterpartyCertificateError.Recognized


