package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.CreatePaymentScheduleError
import io.portone.sdk.server.errors.DeleteBillingKeyError
import io.portone.sdk.server.errors.PayWithBillingKeyError
import io.portone.sdk.server.errors.RevokePaymentSchedulesError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 빌링키가 이미 삭제된 경우 */
@Serializable
@SerialName("BILLING_KEY_ALREADY_DELETED")
@ConsistentCopyVisibility
public data class BillingKeyAlreadyDeletedError internal constructor(
  override val message: String? = null,
): CreatePaymentScheduleError,
  DeleteBillingKeyError,
  PayWithBillingKeyError,
  RevokePaymentSchedulesError
