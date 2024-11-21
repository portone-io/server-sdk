package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("BILLING_KEY_NOT_ISSUED")
internal data class BillingKeyNotIssuedError(
  override val message: String? = null,
) : DeleteBillingKeyError.Recognized
