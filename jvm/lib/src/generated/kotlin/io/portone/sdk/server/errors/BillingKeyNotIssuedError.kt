package io.portone.sdk.server.errors

import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("BILLING_KEY_NOT_ISSUED")
@ConsistentCopyVisibility
public data class BillingKeyNotIssuedError internal constructor(
  val message: String? = null,
) : DeleteBillingKeyError
