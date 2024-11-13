package io.portone.sdk.server.errors

import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** PG사에서 오류를 전달한 경우 */
@Serializable
@SerialName("PG_PROVIDER")
@ConsistentCopyVisibility
public data class PgProviderError internal constructor(
  val pgCode: String,
  val pgMessage: String,
  val message: String? = null,
) : ApplyEscrowLogisticsError, CancelCashReceiptError, CancelPaymentError, CloseVirtualAccountError, ConfirmEscrowError, ConfirmIdentityVerificationError, DeleteBillingKeyError, IssueBillingKeyError, IssueCashReceiptError, ModifyEscrowLogisticsError, PayInstantlyError, PayWithBillingKeyError, RegisterStoreReceiptError, ResendIdentityVerificationError, SendIdentityVerificationError
