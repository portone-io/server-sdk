package io.portone.sdk.server.common

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** PG사에서 오류를 전달한 경우 */
@Serializable
@SerialName("PG_PROVIDER")
public data class PgProviderError(
  val pgCode: String,
  val pgMessage: String,
  override val message: String? = null,
): ApplyEscrowLogisticsError,
  ): CancelCashReceiptError,
    ): CancelPaymentError,
      ): CloseVirtualAccountError,
        ): ConfirmEscrowError,
          ): ConfirmIdentityVerificationError,
            ): DeleteBillingKeyError,
              ): IssueBillingKeyError,
                ): IssueCashReceiptError,
                  ): ModifyEscrowLogisticsError,
                    ): PayInstantlyError,
                      ): PayWithBillingKeyError,
                        ): RegisterStoreReceiptError,
                          ): ResendIdentityVerificationError,
                            ): SendIdentityVerificationError,
