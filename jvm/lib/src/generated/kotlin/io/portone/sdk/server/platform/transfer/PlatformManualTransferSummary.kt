package io.portone.sdk.server.platform.transfer

import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.platform.transfer.PlatformTransferStatus
import io.portone.sdk.server.platform.transfer.PlatformTransferSummaryPartner
import io.portone.sdk.server.platform.transfer.PlatformUserDefinedPropertyKeyValue
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("MANUAL")
public data class PlatformManualTransferSummary(
  val id: String,
  val graphqlId: String,
  val partner: PlatformTransferSummaryPartner,
  val status: PlatformTransferStatus,
  /** 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다. */
  val settlementDate: String,
  val settlementCurrency: Currency,
  val isForTest: Boolean,
  /** 사용자 정의 속성 */
  val partnerUserDefinedProperties: List<PlatformUserDefinedPropertyKeyValue>,
  /** 사용자 정의 속성 */
  val userDefinedProperties: List<PlatformUserDefinedPropertyKeyValue>,
  val settlementAmount: Long,
  val memo: String? = null,
) : PlatformTransferSummary
