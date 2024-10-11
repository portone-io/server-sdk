package io.portone.sdk.server.platform.transfer

import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.platform.PlatformPartner
import io.portone.sdk.server.platform.transfer.PlatformTransfer
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
  val id: String,
  val graphqlId: String,
  /** 파트너 */
  val partner: PlatformPartner,
  /** 정산 상태 */
  val status: PlatformTransferStatus,
  /**
   * 정산 일
   *
   * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
   */
  val settlementDate: String,
  /** 정산 통화 */
  val settlementCurrency: Currency,
  /** 테스트 모드 여부 */
  val isForTest: Boolean,
  /** 사용자 정의 속성 */
  val userDefinedProperties: Array<PlatformUserDefinedPropertyKeyValue>,
  /** 정산 금액 */
  val settlementAmount: Long,
  /** 메모 */
  val memo: String? = null,
  val payoutId: String? = null,
  val payoutGraphqlId: String? = null,
): PlatformTransfer
