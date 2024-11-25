package io.portone.sdk.server.platform.transfer

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 정산 상태 */
@Serializable(PlatformTransferStatusSerializer::class)
public sealed interface PlatformTransferStatus {
  public val value: String
  /** 정산 예약 */
  public data object Scheduled : PlatformTransferStatus {
    override val value: String = "SCHEDULED"
  }
  /** 정산 중 */
  public data object InProcess : PlatformTransferStatus {
    override val value: String = "IN_PROCESS"
  }
  /** 정산 완료 */
  public data object Settled : PlatformTransferStatus {
    override val value: String = "SETTLED"
  }
  /** 지급 중 */
  public data object InPayout : PlatformTransferStatus {
    override val value: String = "IN_PAYOUT"
  }
  /** 지급 완료 */
  public data object PaidOut : PlatformTransferStatus {
    override val value: String = "PAID_OUT"
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformTransferStatus
}


private object PlatformTransferStatusSerializer : KSerializer<PlatformTransferStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformTransferStatus::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PlatformTransferStatus {
    val value = decoder.decodeString()
    return when (value) {
      "SCHEDULED" -> PlatformTransferStatus.Scheduled
      "IN_PROCESS" -> PlatformTransferStatus.InProcess
      "SETTLED" -> PlatformTransferStatus.Settled
      "IN_PAYOUT" -> PlatformTransferStatus.InPayout
      "PAID_OUT" -> PlatformTransferStatus.PaidOut
      else -> PlatformTransferStatus.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PlatformTransferStatus) = encoder.encodeString(value.value)
}
