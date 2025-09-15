package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 정보가 일치하지 않는 경우 */
@Serializable
@SerialName("INFORMATION_MISMATCH")
internal data class InformationMismatchError(
  override val message: String? = null,
) : ConfirmBillingKeyError.Recognized, ConfirmBillingKeyIssueAndPayError.Recognized, ConfirmPaymentError.Recognized


