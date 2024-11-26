package io.portone.sdk.server.platform.bulkpayout

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

@Serializable(PlatformBulkPayoutStatusSerializer::class)
public sealed interface PlatformBulkPayoutStatus {
  public val value: String
  public data object Scheduled : PlatformBulkPayoutStatus {
    override val value: String = "SCHEDULED"
  }
  public data object Preparing : PlatformBulkPayoutStatus {
    override val value: String = "PREPARING"
  }
  public data object Prepared : PlatformBulkPayoutStatus {
    override val value: String = "PREPARED"
  }
  public data object Ongoing : PlatformBulkPayoutStatus {
    override val value: String = "ONGOING"
  }
  public data object Cancelled : PlatformBulkPayoutStatus {
    override val value: String = "CANCELLED"
  }
  public data object Stopped : PlatformBulkPayoutStatus {
    override val value: String = "STOPPED"
  }
  public data object Completed : PlatformBulkPayoutStatus {
    override val value: String = "COMPLETED"
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformBulkPayoutStatus
}


private object PlatformBulkPayoutStatusSerializer : KSerializer<PlatformBulkPayoutStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformBulkPayoutStatus::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PlatformBulkPayoutStatus {
    val value = decoder.decodeString()
    return when (value) {
      "SCHEDULED" -> PlatformBulkPayoutStatus.Scheduled
      "PREPARING" -> PlatformBulkPayoutStatus.Preparing
      "PREPARED" -> PlatformBulkPayoutStatus.Prepared
      "ONGOING" -> PlatformBulkPayoutStatus.Ongoing
      "CANCELLED" -> PlatformBulkPayoutStatus.Cancelled
      "STOPPED" -> PlatformBulkPayoutStatus.Stopped
      "COMPLETED" -> PlatformBulkPayoutStatus.Completed
      else -> PlatformBulkPayoutStatus.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PlatformBulkPayoutStatus) = encoder.encodeString(value.value)
}
