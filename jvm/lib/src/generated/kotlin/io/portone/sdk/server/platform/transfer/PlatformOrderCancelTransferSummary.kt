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
@SerialName("ORDER_CANCEL")
public data class PlatformOrderCancelTransferSummary(
  val id: String,
  val graphqlId: String,
  val storeId: String,
  val partner: PlatformTransferSummaryPartner,
  val status: PlatformTransferStatus,
  /** 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다. */
  val settlementDate: String,
  val settlementCurrency: Currency,
  val isForTest: Boolean,
  /** 사용자 정의 속성 */
  val partnerUserDefinedProperties: Array<PlatformUserDefinedPropertyKeyValue>,
  /** 사용자 정의 속성 */
  val userDefinedProperties: Array<PlatformUserDefinedPropertyKeyValue>,
  val amount: PlatformOrderSettlementAmount,
  val payment: PlatformTransferSummaryPayment,
  /** 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다. */
  val settlementStartDate: String,
  val memo: String? = null,
): PlatformTransferSummary
