package io.portone.sdk.server.b2b.taxinvoice

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 조회 기준 */
@Serializable(B2bSearchDateTypeSerializer::class)
public sealed interface B2bSearchDateType {
  public val value: String
  /** 등록일 */
  @Serializable(RegisterSerializer::class)
  public data object Register : B2bSearchDateType {
    override val value: String = "REGISTER"
  }
  private object RegisterSerializer : KSerializer<Register> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Register::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Register = decoder.decodeString().let {
      if (it != "REGISTER") {
        throw SerializationException(it)
      } else {
        return Register
      }
    }
    override fun serialize(encoder: Encoder, value: Register) = encoder.encodeString(value.value)
  }
  /** 작성일 */
  @Serializable(WriteSerializer::class)
  public data object Write : B2bSearchDateType {
    override val value: String = "WRITE"
  }
  private object WriteSerializer : KSerializer<Write> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Write::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Write = decoder.decodeString().let {
      if (it != "WRITE") {
        throw SerializationException(it)
      } else {
        return Write
      }
    }
    override fun serialize(encoder: Encoder, value: Write) = encoder.encodeString(value.value)
  }
  /** 발행일 */
  @Serializable(IssueSerializer::class)
  public data object Issue : B2bSearchDateType {
    override val value: String = "ISSUE"
  }
  private object IssueSerializer : KSerializer<Issue> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Issue::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Issue = decoder.decodeString().let {
      if (it != "ISSUE") {
        throw SerializationException(it)
      } else {
        return Issue
      }
    }
    override fun serialize(encoder: Encoder, value: Issue) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : B2bSearchDateType
}


private object B2bSearchDateTypeSerializer : KSerializer<B2bSearchDateType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(B2bSearchDateType::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): B2bSearchDateType {
    val value = decoder.decodeString()
    return when (value) {
      "REGISTER" -> B2bSearchDateType.Register
      "WRITE" -> B2bSearchDateType.Write
      "ISSUE" -> B2bSearchDateType.Issue
      else -> B2bSearchDateType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: B2bSearchDateType) = encoder.encodeString(value.value)
}
