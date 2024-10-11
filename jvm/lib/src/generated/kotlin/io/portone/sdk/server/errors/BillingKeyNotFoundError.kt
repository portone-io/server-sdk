package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.CreatePaymentScheduleError
import io.portone.sdk.server.errors.DeleteBillingKeyError
import io.portone.sdk.server.errors.GetBillingKeyInfoError
import io.portone.sdk.server.errors.PayWithBillingKeyError
import io.portone.sdk.server.errors.RevokePaymentSchedulesError
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 빌링키가 존재하지 않는 경우 */
@Serializable
@SerialName("BILLING_KEY_NOT_FOUND")
public data class BillingKeyNotFoundError(
  val message: String? = null,
): CreatePaymentScheduleError,
  DeleteBillingKeyError,
  GetBillingKeyInfoError,
  PayWithBillingKeyError,
  RevokePaymentSchedulesError
