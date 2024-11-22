package io.portone.sdk.server.identityverification

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 본인인증 통신사 */
@Serializable(IdentityVerificationOperatorSerializer::class)
public sealed interface IdentityVerificationOperator {
  public val value: String
  /** SKT */
  public data object Skt : IdentityVerificationOperator {
    override val value: String = "SKT"
  }
  /** KT */
  public data object Kt : IdentityVerificationOperator {
    override val value: String = "KT"
  }
  /** LGU */
  public data object Lgu : IdentityVerificationOperator {
    override val value: String = "LGU"
  }
  /** SKT 알뜰폰 */
  public data object SktMvno : IdentityVerificationOperator {
    override val value: String = "SKT_MVNO"
  }
  /** KT 알뜰폰 */
  public data object KtMvno : IdentityVerificationOperator {
    override val value: String = "KT_MVNO"
  }
  /** LGU 알뜰폰 */
  public data object LguMvno : IdentityVerificationOperator {
    override val value: String = "LGU_MVNO"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : IdentityVerificationOperator
}


private object IdentityVerificationOperatorSerializer : KSerializer<IdentityVerificationOperator> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(IdentityVerificationOperator::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): IdentityVerificationOperator {
    val value = decoder.decodeString()
    return when (value) {
      "SKT" -> IdentityVerificationOperator.Skt
      "KT" -> IdentityVerificationOperator.Kt
      "LGU" -> IdentityVerificationOperator.Lgu
      "SKT_MVNO" -> IdentityVerificationOperator.SktMvno
      "KT_MVNO" -> IdentityVerificationOperator.KtMvno
      "LGU_MVNO" -> IdentityVerificationOperator.LguMvno
      else -> IdentityVerificationOperator.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: IdentityVerificationOperator) = encoder.encodeString(value.value)
}
