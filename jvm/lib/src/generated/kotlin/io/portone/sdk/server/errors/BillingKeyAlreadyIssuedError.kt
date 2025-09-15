package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("BILLING_KEY_ALREADY_ISSUED")
internal data class BillingKeyAlreadyIssuedError(
  override val message: String? = null,
) : ConfirmBillingKeyError.Recognized, ConfirmBillingKeyIssueAndPayError.Recognized


