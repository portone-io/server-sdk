package io.portone.sdk.server.billingkey

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("BILLING_KEY_NOT_ISSUED")
public data class BillingKeyNotIssuedError(
  override val message: String? = null,
): DeleteBillingKeyError,
