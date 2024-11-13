package io.portone.sdk.server.errors

import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 빌링키가 존재하지 않는 경우 */
@Serializable
@SerialName("BILLING_KEY_NOT_FOUND")
@ConsistentCopyVisibility
public data class BillingKeyNotFoundError internal constructor(
  val message: String? = null,
) : CreatePaymentScheduleError, DeleteBillingKeyError, GetBillingKeyInfoError, PayWithBillingKeyError, RevokePaymentSchedulesError
