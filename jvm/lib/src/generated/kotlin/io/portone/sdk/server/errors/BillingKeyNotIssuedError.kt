package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.DeleteBillingKeyError
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("BILLING_KEY_NOT_ISSUED")
public data class BillingKeyNotIssuedError(
  val message: String? = null,
): DeleteBillingKeyError
