package io.portone.sdk.server.common

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 빌링키가 이미 삭제된 경우 */
@Serializable
@SerialName("BILLING_KEY_ALREADY_DELETED")
public data class BillingKeyAlreadyDeletedError(
  override val message: String? = null,
): CreatePaymentScheduleError,
  ): DeleteBillingKeyError,
    ): PayWithBillingKeyError,
      ): RevokePaymentSchedulesError,
