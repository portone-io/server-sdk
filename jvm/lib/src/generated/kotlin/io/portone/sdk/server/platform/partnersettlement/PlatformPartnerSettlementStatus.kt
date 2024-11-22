package io.portone.sdk.server.platform.partnersettlement

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 정산 상태 */
@Serializable(PlatformPartnerSettlementStatusSerializer::class)
public sealed interface PlatformPartnerSettlementStatus {
  public val value: String
  /** 지급 예약 */
  public data object PayoutScheduled : PlatformPartnerSettlementStatus {
    override val value: String = "PAYOUT_SCHEDULED"
  }
  /** 지급 예정 */
  public data object PayoutPrepared : PlatformPartnerSettlementStatus {
    override val value: String = "PAYOUT_PREPARED"
  }
  /** 지급 보류 */
  public data object PayoutWithheld : PlatformPartnerSettlementStatus {
    override val value: String = "PAYOUT_WITHHELD"
  }
  /** 지급 실패 */
  public data object PayoutFailed : PlatformPartnerSettlementStatus {
    override val value: String = "PAYOUT_FAILED"
  }
  /** 지급 중 */
  public data object InPayout : PlatformPartnerSettlementStatus {
    override val value: String = "IN_PAYOUT"
  }
  /** 지급 완료 */
  public data object PaidOut : PlatformPartnerSettlementStatus {
    override val value: String = "PAID_OUT"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformPartnerSettlementStatus
}


private object PlatformPartnerSettlementStatusSerializer : KSerializer<PlatformPartnerSettlementStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformPartnerSettlementStatus::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PlatformPartnerSettlementStatus {
    val value = decoder.decodeString()
    return when (value) {
      "PAYOUT_SCHEDULED" -> PlatformPartnerSettlementStatus.PayoutScheduled
      "PAYOUT_PREPARED" -> PlatformPartnerSettlementStatus.PayoutPrepared
      "PAYOUT_WITHHELD" -> PlatformPartnerSettlementStatus.PayoutWithheld
      "PAYOUT_FAILED" -> PlatformPartnerSettlementStatus.PayoutFailed
      "IN_PAYOUT" -> PlatformPartnerSettlementStatus.InPayout
      "PAID_OUT" -> PlatformPartnerSettlementStatus.PaidOut
      else -> PlatformPartnerSettlementStatus.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PlatformPartnerSettlementStatus) = encoder.encodeString(value.value)
}
