package io.portone.sdk.server.platform.partner

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

@Serializable(PlatformBulkTaskTypeSerializer::class)
public sealed interface PlatformBulkTaskType {
  public val value: String
  @Serializable(CreateTransfersSerializer::class)
  public data object CreateTransfers : PlatformBulkTaskType {
    override val value: String = "CREATE_TRANSFERS"
  }
  private object CreateTransfersSerializer : KSerializer<CreateTransfers> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(CreateTransfers::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): CreateTransfers = decoder.decodeString().let {
      if (it != "CREATE_TRANSFERS") {
        throw SerializationException(it)
      } else {
        return CreateTransfers
      }
    }
    override fun serialize(encoder: Encoder, value: CreateTransfers) = encoder.encodeString(value.value)
  }
  @Serializable(CreatePartnersSerializer::class)
  public data object CreatePartners : PlatformBulkTaskType {
    override val value: String = "CREATE_PARTNERS"
  }
  private object CreatePartnersSerializer : KSerializer<CreatePartners> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(CreatePartners::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): CreatePartners = decoder.decodeString().let {
      if (it != "CREATE_PARTNERS") {
        throw SerializationException(it)
      } else {
        return CreatePartners
      }
    }
    override fun serialize(encoder: Encoder, value: CreatePartners) = encoder.encodeString(value.value)
  }
  @Serializable(ConnectMemberCompaniesSerializer::class)
  public data object ConnectMemberCompanies : PlatformBulkTaskType {
    override val value: String = "CONNECT_MEMBER_COMPANIES"
  }
  private object ConnectMemberCompaniesSerializer : KSerializer<ConnectMemberCompanies> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(ConnectMemberCompanies::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): ConnectMemberCompanies = decoder.decodeString().let {
      if (it != "CONNECT_MEMBER_COMPANIES") {
        throw SerializationException(it)
      } else {
        return ConnectMemberCompanies
      }
    }
    override fun serialize(encoder: Encoder, value: ConnectMemberCompanies) = encoder.encodeString(value.value)
  }
  @Serializable(DisconnectMemberCompaniesSerializer::class)
  public data object DisconnectMemberCompanies : PlatformBulkTaskType {
    override val value: String = "DISCONNECT_MEMBER_COMPANIES"
  }
  private object DisconnectMemberCompaniesSerializer : KSerializer<DisconnectMemberCompanies> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(DisconnectMemberCompanies::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): DisconnectMemberCompanies = decoder.decodeString().let {
      if (it != "DISCONNECT_MEMBER_COMPANIES") {
        throw SerializationException(it)
      } else {
        return DisconnectMemberCompanies
      }
    }
    override fun serialize(encoder: Encoder, value: DisconnectMemberCompanies) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  public data class Unrecognized internal constructor(override val value: String) : PlatformBulkTaskType
}


private object PlatformBulkTaskTypeSerializer : KSerializer<PlatformBulkTaskType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformBulkTaskType::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PlatformBulkTaskType {
    val value = decoder.decodeString()
    return when (value) {
      "CREATE_TRANSFERS" -> PlatformBulkTaskType.CreateTransfers
      "CREATE_PARTNERS" -> PlatformBulkTaskType.CreatePartners
      "CONNECT_MEMBER_COMPANIES" -> PlatformBulkTaskType.ConnectMemberCompanies
      "DISCONNECT_MEMBER_COMPANIES" -> PlatformBulkTaskType.DisconnectMemberCompanies
      else -> PlatformBulkTaskType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PlatformBulkTaskType) = encoder.encodeString(value.value)
}
