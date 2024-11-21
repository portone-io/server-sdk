package io.portone.sdk.server.payment

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/**
 * 웹훅 실행 트리거
 *
 * 수동 웹훅 재발송, 가상계좌 입금, 비동기 취소 승인 시 발생한 웹훅일 때 필드의 값이 존재합니다.
 */
@Serializable
public sealed interface PaymentWebhookTrigger {
  public val value: String
  @SerialName("MANUAL")
  public data object Manual : PaymentWebhookTrigger {
    override val value: String = "MANUAL"
  }
  @SerialName("VIRTUAL_ACCOUNT_DEPOSIT")
  public data object VirtualAccountDeposit : PaymentWebhookTrigger {
    override val value: String = "VIRTUAL_ACCOUNT_DEPOSIT"
  }
  @SerialName("ASYNC_CANCEL_APPROVED")
  public data object AsyncCancelApproved : PaymentWebhookTrigger {
    override val value: String = "ASYNC_CANCEL_APPROVED"
  }
  @SerialName("ASYNC_CANCEL_FAILED")
  public data object AsyncCancelFailed : PaymentWebhookTrigger {
    override val value: String = "ASYNC_CANCEL_FAILED"
  }
  @SerialName("ASYNC_PAY_APPROVED")
  public data object AsyncPayApproved : PaymentWebhookTrigger {
    override val value: String = "ASYNC_PAY_APPROVED"
  }
  @SerialName("ASYNC_PAY_FAILED")
  public data object AsyncPayFailed : PaymentWebhookTrigger {
    override val value: String = "ASYNC_PAY_FAILED"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PaymentWebhookTrigger
}
