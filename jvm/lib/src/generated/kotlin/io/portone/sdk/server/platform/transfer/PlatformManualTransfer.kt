package io.portone.sdk.server.platform.transfer

import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.platform.PlatformPartner
import io.portone.sdk.server.platform.transfer.PlatformTransferStatus
import io.portone.sdk.server.platform.transfer.PlatformUserDefinedPropertyKeyValue
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 수기 정산건 */
@Serializable
@SerialName("MANUAL")
public data class PlatformManualTransfer(
  /** 정산건 아이디 */
  override val id: String,
  override val graphqlId: String,
  /** 파트너 */
  override val partner: PlatformPartner,
  /** 정산 상태 */
  override val status: PlatformTransferStatus,
  /** 메모 */
  override val memo: String? = null,
  /**
   * 정산 일
   *
   * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
   */
  override val settlementDate: String,
  /** 정산 통화 */
  override val settlementCurrency: Currency,
  override val payoutId: String? = null,
  override val payoutGraphqlId: String? = null,
  /** 테스트 모드 여부 */
  override val isForTest: Boolean,
  /** 사용자 정의 속성 */
  override val userDefinedProperties: List<PlatformUserDefinedPropertyKeyValue>,
  /** 정산 금액 */
  val settlementAmount: Long,
) : PlatformTransfer.Recognized
