package io.portone.sdk.server.payment

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/**
 * 웹훅 실행 트리거
 *
 * 수동 웹훅 재발송, 가상계좌 입금, 비동기 취소 승인 시 발생한 웹훅일 때 필드의 값이 존재합니다.
 */
@Serializable(PaymentWebhookTriggerSerializer::class)
public sealed interface PaymentWebhookTrigger {
  public val value: String
  public data object Manual : PaymentWebhookTrigger {
    override val value: String = "MANUAL"
  }
  public data object VirtualAccountDeposit : PaymentWebhookTrigger {
    override val value: String = "VIRTUAL_ACCOUNT_DEPOSIT"
  }
  public data object AsyncCancelApproved : PaymentWebhookTrigger {
    override val value: String = "ASYNC_CANCEL_APPROVED"
  }
  public data object AsyncCancelFailed : PaymentWebhookTrigger {
    override val value: String = "ASYNC_CANCEL_FAILED"
  }
  public data object AsyncPayApproved : PaymentWebhookTrigger {
    override val value: String = "ASYNC_PAY_APPROVED"
  }
  public data object AsyncPayFailed : PaymentWebhookTrigger {
    override val value: String = "ASYNC_PAY_FAILED"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PaymentWebhookTrigger
}


private object PaymentWebhookTriggerSerializer : KSerializer<PaymentWebhookTrigger> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PaymentWebhookTrigger::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PaymentWebhookTrigger {
    val value = decoder.decodeString()
    return when (value) {
      "MANUAL" -> PaymentWebhookTrigger.Manual
      "VIRTUAL_ACCOUNT_DEPOSIT" -> PaymentWebhookTrigger.VirtualAccountDeposit
      "ASYNC_CANCEL_APPROVED" -> PaymentWebhookTrigger.AsyncCancelApproved
      "ASYNC_CANCEL_FAILED" -> PaymentWebhookTrigger.AsyncCancelFailed
      "ASYNC_PAY_APPROVED" -> PaymentWebhookTrigger.AsyncPayApproved
      "ASYNC_PAY_FAILED" -> PaymentWebhookTrigger.AsyncPayFailed
      else -> PaymentWebhookTrigger.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PaymentWebhookTrigger) = encoder.encodeString(value.value)
}
