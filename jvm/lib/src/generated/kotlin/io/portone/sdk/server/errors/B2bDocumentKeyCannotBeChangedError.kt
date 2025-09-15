package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 문서번호 수정이 요청된 경우 */
@Serializable
@SerialName("B2B_DOCUMENT_KEY_CANNOT_BE_CHANGED")
internal data class B2bDocumentKeyCannotBeChangedError(
  override val message: String? = null,
) : UpdateB2bTaxInvoiceDraftError.Recognized


