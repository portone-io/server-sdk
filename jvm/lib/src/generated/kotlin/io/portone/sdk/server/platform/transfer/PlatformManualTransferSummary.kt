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
  override val id: String,
  override val graphqlId: String,
  override val partner: PlatformTransferSummaryPartner,
  override val status: PlatformTransferStatus,
  override val memo: String? = null,
  /** 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다. */
  override val settlementDate: String,
  override val settlementCurrency: Currency,
  override val isForTest: Boolean,
  /** 사용자 정의 속성 */
  override val partnerUserDefinedProperties: List<PlatformUserDefinedPropertyKeyValue>,
  /** 사용자 정의 속성 */
  override val userDefinedProperties: List<PlatformUserDefinedPropertyKeyValue>,
  val settlementAmount: Long,
) : PlatformTransferSummary.Recognized


