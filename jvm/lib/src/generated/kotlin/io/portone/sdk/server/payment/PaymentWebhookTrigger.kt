package io.portone.sdk.server.payment

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
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
  @Serializable(ManualSerializer::class)
  public data object Manual : PaymentWebhookTrigger {
    override val value: String = "MANUAL"
  }
  private object ManualSerializer : KSerializer<Manual> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Manual::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Manual = decoder.decodeString().let {
      if (it != "MANUAL") {
        throw SerializationException(it)
      } else {
        return Manual
      }
    }
    override fun serialize(encoder: Encoder, value: Manual) = encoder.encodeString(value.value)
  }
  @Serializable(VirtualAccountDepositSerializer::class)
  public data object VirtualAccountDeposit : PaymentWebhookTrigger {
    override val value: String = "VIRTUAL_ACCOUNT_DEPOSIT"
  }
  private object VirtualAccountDepositSerializer : KSerializer<VirtualAccountDeposit> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(VirtualAccountDeposit::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): VirtualAccountDeposit = decoder.decodeString().let {
      if (it != "VIRTUAL_ACCOUNT_DEPOSIT") {
        throw SerializationException(it)
      } else {
        return VirtualAccountDeposit
      }
    }
    override fun serialize(encoder: Encoder, value: VirtualAccountDeposit) = encoder.encodeString(value.value)
  }
  @Serializable(AsyncCancelApprovedSerializer::class)
  public data object AsyncCancelApproved : PaymentWebhookTrigger {
    override val value: String = "ASYNC_CANCEL_APPROVED"
  }
  private object AsyncCancelApprovedSerializer : KSerializer<AsyncCancelApproved> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(AsyncCancelApproved::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): AsyncCancelApproved = decoder.decodeString().let {
      if (it != "ASYNC_CANCEL_APPROVED") {
        throw SerializationException(it)
      } else {
        return AsyncCancelApproved
      }
    }
    override fun serialize(encoder: Encoder, value: AsyncCancelApproved) = encoder.encodeString(value.value)
  }
  @Serializable(AsyncCancelFailedSerializer::class)
  public data object AsyncCancelFailed : PaymentWebhookTrigger {
    override val value: String = "ASYNC_CANCEL_FAILED"
  }
  private object AsyncCancelFailedSerializer : KSerializer<AsyncCancelFailed> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(AsyncCancelFailed::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): AsyncCancelFailed = decoder.decodeString().let {
      if (it != "ASYNC_CANCEL_FAILED") {
        throw SerializationException(it)
      } else {
        return AsyncCancelFailed
      }
    }
    override fun serialize(encoder: Encoder, value: AsyncCancelFailed) = encoder.encodeString(value.value)
  }
  @Serializable(AsyncPayApprovedSerializer::class)
  public data object AsyncPayApproved : PaymentWebhookTrigger {
    override val value: String = "ASYNC_PAY_APPROVED"
  }
  private object AsyncPayApprovedSerializer : KSerializer<AsyncPayApproved> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(AsyncPayApproved::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): AsyncPayApproved = decoder.decodeString().let {
      if (it != "ASYNC_PAY_APPROVED") {
        throw SerializationException(it)
      } else {
        return AsyncPayApproved
      }
    }
    override fun serialize(encoder: Encoder, value: AsyncPayApproved) = encoder.encodeString(value.value)
  }
  @Serializable(AsyncPayFailedSerializer::class)
  public data object AsyncPayFailed : PaymentWebhookTrigger {
    override val value: String = "ASYNC_PAY_FAILED"
  }
  private object AsyncPayFailedSerializer : KSerializer<AsyncPayFailed> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(AsyncPayFailed::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): AsyncPayFailed = decoder.decodeString().let {
      if (it != "ASYNC_PAY_FAILED") {
        throw SerializationException(it)
      } else {
        return AsyncPayFailed
      }
    }
    override fun serialize(encoder: Encoder, value: AsyncPayFailed) = encoder.encodeString(value.value)
  }
  @Serializable(DisputeCreatedSerializer::class)
  public data object DisputeCreated : PaymentWebhookTrigger {
    override val value: String = "DISPUTE_CREATED"
  }
  private object DisputeCreatedSerializer : KSerializer<DisputeCreated> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(DisputeCreated::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): DisputeCreated = decoder.decodeString().let {
      if (it != "DISPUTE_CREATED") {
        throw SerializationException(it)
      } else {
        return DisputeCreated
      }
    }
    override fun serialize(encoder: Encoder, value: DisputeCreated) = encoder.encodeString(value.value)
  }
  @Serializable(DisputeResolvedSerializer::class)
  public data object DisputeResolved : PaymentWebhookTrigger {
    override val value: String = "DISPUTE_RESOLVED"
  }
  private object DisputeResolvedSerializer : KSerializer<DisputeResolved> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(DisputeResolved::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): DisputeResolved = decoder.decodeString().let {
      if (it != "DISPUTE_RESOLVED") {
        throw SerializationException(it)
      } else {
        return DisputeResolved
      }
    }
    override fun serialize(encoder: Encoder, value: DisputeResolved) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  public data class Unrecognized internal constructor(override val value: String) : PaymentWebhookTrigger
}


private object PaymentWebhookTriggerSerializer : KSerializer<PaymentWebhookTrigger> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PaymentWebhookTrigger::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PaymentWebhookTrigger {
    val value = decoder.decodeString()
    return when (value) {
      "MANUAL" -> PaymentWebhookTrigger.Manual
      "VIRTUAL_ACCOUNT_DEPOSIT" -> PaymentWebhookTrigger.VirtualAccountDeposit
      "ASYNC_CANCEL_APPROVED" -> PaymentWebhookTrigger.AsyncCancelApproved
      "ASYNC_CANCEL_FAILED" -> PaymentWebhookTrigger.AsyncCancelFailed
      "ASYNC_PAY_APPROVED" -> PaymentWebhookTrigger.AsyncPayApproved
      "ASYNC_PAY_FAILED" -> PaymentWebhookTrigger.AsyncPayFailed
      "DISPUTE_CREATED" -> PaymentWebhookTrigger.DisputeCreated
      "DISPUTE_RESOLVED" -> PaymentWebhookTrigger.DisputeResolved
      else -> PaymentWebhookTrigger.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PaymentWebhookTrigger) = encoder.encodeString(value.value)
}
