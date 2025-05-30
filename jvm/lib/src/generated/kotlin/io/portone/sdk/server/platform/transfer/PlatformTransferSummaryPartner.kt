package io.portone.sdk.server.platform.transfer

import io.portone.sdk.server.platform.PlatformPartnerTaxationType
import io.portone.sdk.server.platform.transfer.PlatformTransferSummaryPartnerType
import io.portone.sdk.server.platform.transfer.PlatformUserDefinedPropertyKeyValue
import kotlin.String
import kotlinx.serialization.Serializable

@Serializable
public data class PlatformTransferSummaryPartner(
  val id: String,
  val graphqlId: String,
  val name: String,
  val type: PlatformTransferSummaryPartnerType,
  val taxationType: PlatformPartnerTaxationType? = null,
  /** 사용자 정의 속성 */
  val userDefinedProperties: List<PlatformUserDefinedPropertyKeyValue>,
)


