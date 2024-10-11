package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PayInstantlyError
import io.portone.sdk.server.errors.PayWithBillingKeyError
import io.portone.sdk.server.errors.PreRegisterPaymentError
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 결제가 이미 완료된 경우 */
@Serializable
@SerialName("ALREADY_PAID")
public data class AlreadyPaidError(
  override val message: String? = null,
): PayInstantlyError,
  PayWithBillingKeyError,
  PreRegisterPaymentError