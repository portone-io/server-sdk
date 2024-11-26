package io.portone.sdk.server.identityverification

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 본인인증 방식 */
@Serializable(IdentityVerificationMethodSerializer::class)
public sealed interface IdentityVerificationMethod {
  public val value: String
  public data object Sms : IdentityVerificationMethod {
    override val value: String = "SMS"
  }
  public data object App : IdentityVerificationMethod {
    override val value: String = "APP"
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : IdentityVerificationMethod
}


private object IdentityVerificationMethodSerializer : KSerializer<IdentityVerificationMethod> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(IdentityVerificationMethod::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): IdentityVerificationMethod {
    val value = decoder.decodeString()
    return when (value) {
      "SMS" -> IdentityVerificationMethod.Sms
      "APP" -> IdentityVerificationMethod.App
      else -> IdentityVerificationMethod.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: IdentityVerificationMethod) = encoder.encodeString(value.value)
}
