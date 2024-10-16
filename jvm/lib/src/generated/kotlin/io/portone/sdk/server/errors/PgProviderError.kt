package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.ApplyEscrowLogisticsError
import io.portone.sdk.server.errors.CancelCashReceiptError
import io.portone.sdk.server.errors.CancelPaymentError
import io.portone.sdk.server.errors.CloseVirtualAccountError
import io.portone.sdk.server.errors.ConfirmEscrowError
import io.portone.sdk.server.errors.ConfirmIdentityVerificationError
import io.portone.sdk.server.errors.DeleteBillingKeyError
import io.portone.sdk.server.errors.IssueBillingKeyError
import io.portone.sdk.server.errors.IssueCashReceiptError
import io.portone.sdk.server.errors.ModifyEscrowLogisticsError
import io.portone.sdk.server.errors.PayInstantlyError
import io.portone.sdk.server.errors.PayWithBillingKeyError
import io.portone.sdk.server.errors.RegisterStoreReceiptError
import io.portone.sdk.server.errors.ResendIdentityVerificationError
import io.portone.sdk.server.errors.SendIdentityVerificationError
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
  override val message: String? = null,
): ApplyEscrowLogisticsError,
  CancelCashReceiptError,
  CancelPaymentError,
  CloseVirtualAccountError,
  ConfirmEscrowError,
  ConfirmIdentityVerificationError,
  DeleteBillingKeyError,
  IssueBillingKeyError,
  IssueCashReceiptError,
  ModifyEscrowLogisticsError,
  PayInstantlyError,
  PayWithBillingKeyError,
  RegisterStoreReceiptError,
  ResendIdentityVerificationError,
  SendIdentityVerificationError
