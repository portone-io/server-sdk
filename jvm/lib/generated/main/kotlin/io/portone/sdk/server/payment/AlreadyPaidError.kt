package io.portone.sdk.server.payment

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 결제가 이미 완료된 경우 */
@Serializable
@SerialName("ALREADY_PAID")
public data class AlreadyPaidError(
  override val message: String? = null,
): PayInstantlyError,
  ): PayWithBillingKeyError,
    ): PreRegisterPaymentError,
