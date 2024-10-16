package io.portone.sdk.server.platform.transfer

import io.portone.sdk.server.platform.transfer.PlatformUserDefinedPropertyKeyValue
import kotlin.String
import kotlinx.serialization.Serializable

/** 수기 정산건 생성을 위한 입력 정보 */
@Serializable
internal data class CreatePlatformManualTransferBody(
  /** 파트너 아이디 */
  val partnerId: String,
  /** 정산 금액 */
  val settlementAmount: Long,
  /**
   * 정산 일
   *
   * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
   */
  val settlementDate: String,
  /** 메모 */
  val memo: String? = null,
  /**
   * 테스트 모드 여부
   *
   * 기본값은 false 입니다.
   */
  val isForTest: Boolean? = null,
  /** 사용자 정의 속성 */
  val userDefinedProperties: List<PlatformUserDefinedPropertyKeyValue>? = null,
)
