package io.portone.sdk.server.platform.transfer

import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.platform.transfer.PlatformTransferStatus
import io.portone.sdk.server.platform.transfer.PlatformTransferSummaryPartner
import io.portone.sdk.server.platform.transfer.PlatformUserDefinedPropertyKeyValue
import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

@Serializable
@JsonClassDiscriminator("type")
public sealed interface PlatformTransferSummary {
  public val id: String
  public val graphqlId: String
  public val partner: PlatformTransferSummaryPartner
  public val status: PlatformTransferStatus
  public val memo: String?
  /** 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다. */
  public val settlementDate: String
  public val settlementCurrency: Currency
  public val isForTest: Boolean
  /** 사용자 정의 속성 */
  public val partnerUserDefinedProperties: List<PlatformUserDefinedPropertyKeyValue>
  /** 사용자 정의 속성 */
  public val userDefinedProperties: List<PlatformUserDefinedPropertyKeyValue>
}
