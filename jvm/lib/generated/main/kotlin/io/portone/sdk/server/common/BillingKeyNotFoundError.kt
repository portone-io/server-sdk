package io.portone.sdk.server.common

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 빌링키가 존재하지 않는 경우 */
@Serializable
@SerialName("BILLING_KEY_NOT_FOUND")
public data class BillingKeyNotFoundError(
  override val message: String? = null,
): CreatePaymentScheduleError,
  ): DeleteBillingKeyError,
    ): GetBillingKeyInfoError,
      ): PayWithBillingKeyError,
        ): RevokePaymentSchedulesError,
