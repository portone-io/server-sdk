package io.portone.sdk.server.identityverification

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 본인인증 방식 */
@Serializable(IdentityVerificationMethodSerializer::class)
public sealed interface IdentityVerificationMethod {
  public val value: String
  @Serializable(SmsSerializer::class)
  public data object Sms : IdentityVerificationMethod {
    override val value: String = "SMS"
  }
  private object SmsSerializer : KSerializer<Sms> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Sms::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Sms = decoder.decodeString().let {
      if (it != "SMS") {
        throw SerializationException(it)
      } else {
        return Sms
      }
    }
    override fun serialize(encoder: Encoder, value: Sms) = encoder.encodeString(value.value)
  }
  @Serializable(AppSerializer::class)
  public data object App : IdentityVerificationMethod {
    override val value: String = "APP"
  }
  private object AppSerializer : KSerializer<App> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(App::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): App = decoder.decodeString().let {
      if (it != "APP") {
        throw SerializationException(it)
      } else {
        return App
      }
    }
    override fun serialize(encoder: Encoder, value: App) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  public data class Unrecognized internal constructor(override val value: String) : IdentityVerificationMethod
}


private object IdentityVerificationMethodSerializer : KSerializer<IdentityVerificationMethod> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(IdentityVerificationMethod::class.java.name, PrimitiveKind.STRING)
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
