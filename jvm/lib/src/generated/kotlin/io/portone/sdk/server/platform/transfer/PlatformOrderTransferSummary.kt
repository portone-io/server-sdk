package io.portone.sdk.server.platform.transfer

import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.platform.PlatformOrderSettlementAmount
import io.portone.sdk.server.platform.transfer.PlatformTransferStatus
import io.portone.sdk.server.platform.transfer.PlatformTransferSummary
import io.portone.sdk.server.platform.transfer.PlatformTransferSummaryPartner
import io.portone.sdk.server.platform.transfer.PlatformTransferSummaryPayment
import io.portone.sdk.server.platform.transfer.PlatformUserDefinedPropertyKeyValue
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("ORDER")
public data class PlatformOrderTransferSummary(
  override val id: String,
  override val graphqlId: String,
  val storeId: String,
  override val partner: PlatformTransferSummaryPartner,
  override val status: PlatformTransferStatus,
  /** 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다. */
  override val settlementDate: String,
  override val settlementCurrency: Currency,
  override val isForTest: Boolean,
  /** 사용자 정의 속성 */
  override val partnerUserDefinedProperties: List<PlatformUserDefinedPropertyKeyValue>,
  /** 사용자 정의 속성 */
  override val userDefinedProperties: List<PlatformUserDefinedPropertyKeyValue>,
  val amount: PlatformOrderSettlementAmount,
  val payment: PlatformTransferSummaryPayment,
  /** 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다. */
  val settlementStartDate: String,
  override val memo: String? = null,
): PlatformTransferSummary