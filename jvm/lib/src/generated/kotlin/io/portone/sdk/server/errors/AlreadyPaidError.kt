package io.portone.sdk.server.errors

import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 결제가 이미 완료된 경우 */
@Serializable
@SerialName("ALREADY_PAID")
@ConsistentCopyVisibility
public data class AlreadyPaidError internal constructor(
  val message: String? = null,
) : PayInstantlyError, PayWithBillingKeyError, PreRegisterPaymentError
