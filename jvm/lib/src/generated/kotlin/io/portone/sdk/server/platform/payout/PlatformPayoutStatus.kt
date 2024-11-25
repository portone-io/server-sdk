package io.portone.sdk.server.platform.payout

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

@Serializable(PlatformPayoutStatusSerializer::class)
public sealed interface PlatformPayoutStatus {
  public val value: String
  public data object Prepared : PlatformPayoutStatus {
    override val value: String = "PREPARED"
  }
  public data object Cancelled : PlatformPayoutStatus {
    override val value: String = "CANCELLED"
  }
  public data object Stopped : PlatformPayoutStatus {
    override val value: String = "STOPPED"
  }
  public data object Processing : PlatformPayoutStatus {
    override val value: String = "PROCESSING"
  }
  public data object Succeeded : PlatformPayoutStatus {
    override val value: String = "SUCCEEDED"
  }
  public data object Failed : PlatformPayoutStatus {
    override val value: String = "FAILED"
  }
  public data object Scheduled : PlatformPayoutStatus {
    override val value: String = "SCHEDULED"
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformPayoutStatus
}


private object PlatformPayoutStatusSerializer : KSerializer<PlatformPayoutStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformPayoutStatus::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PlatformPayoutStatus {
    val value = decoder.decodeString()
    return when (value) {
      "PREPARED" -> PlatformPayoutStatus.Prepared
      "CANCELLED" -> PlatformPayoutStatus.Cancelled
      "STOPPED" -> PlatformPayoutStatus.Stopped
      "PROCESSING" -> PlatformPayoutStatus.Processing
      "SUCCEEDED" -> PlatformPayoutStatus.Succeeded
      "FAILED" -> PlatformPayoutStatus.Failed
      "SCHEDULED" -> PlatformPayoutStatus.Scheduled
      else -> PlatformPayoutStatus.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PlatformPayoutStatus) = encoder.encodeString(value.value)
}
