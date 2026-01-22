package io.portone.sdk.server.payment

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 결제 취소 요청 주체 */
@Serializable(CancelRequesterSerializer::class)
public sealed interface CancelRequester {
  public val value: String
  /** 구매자 */
  @Serializable(CustomerSerializer::class)
  public data object Customer : CancelRequester {
    override val value: String = "CUSTOMER"
  }
  public object CustomerSerializer : KSerializer<Customer> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Customer::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Customer = decoder.decodeString().let {
      if (it != "CUSTOMER") {
        throw SerializationException(it)
      } else {
        return Customer
      }
    }
    override fun serialize(encoder: Encoder, value: Customer): Unit = encoder.encodeString(value.value)
  }
  /** 관리자 */
  @Serializable(AdminSerializer::class)
  public data object Admin : CancelRequester {
    override val value: String = "ADMIN"
  }
  public object AdminSerializer : KSerializer<Admin> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Admin::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Admin = decoder.decodeString().let {
      if (it != "ADMIN") {
        throw SerializationException(it)
      } else {
        return Admin
      }
    }
    override fun serialize(encoder: Encoder, value: Admin): Unit = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : CancelRequester
}


public object CancelRequesterSerializer : KSerializer<CancelRequester> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(CancelRequester::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): CancelRequester {
    val value = decoder.decodeString()
    return when (value) {
      "CUSTOMER" -> CancelRequester.Customer
      "ADMIN" -> CancelRequester.Admin
      else -> CancelRequester.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: CancelRequester): Unit = encoder.encodeString(value.value)
}
