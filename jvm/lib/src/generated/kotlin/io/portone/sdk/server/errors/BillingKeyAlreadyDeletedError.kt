package io.portone.sdk.server.errors

import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 빌링키가 이미 삭제된 경우 */
@Serializable
@SerialName("BILLING_KEY_ALREADY_DELETED")
@ConsistentCopyVisibility
public data class BillingKeyAlreadyDeletedError internal constructor(
  val message: String? = null,
) : CreatePaymentScheduleError, DeleteBillingKeyError, PayWithBillingKeyError, RevokePaymentSchedulesError
