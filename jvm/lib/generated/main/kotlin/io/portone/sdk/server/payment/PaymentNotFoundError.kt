package io.portone.sdk.server.payment

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 결제 건이 존재하지 않는 경우 */
@Serializable
@SerialName("PAYMENT_NOT_FOUND")
public data class PaymentNotFoundError(
  override val message: String? = null,
): ApplyEscrowLogisticsError,
  ): CancelPaymentError,
    ): CloseVirtualAccountError,
      ): ConfirmEscrowError,
        ): GetPaymentError,
          ): ModifyEscrowLogisticsError,
            ): RegisterStoreReceiptError,
              ): ResendWebhookError,
