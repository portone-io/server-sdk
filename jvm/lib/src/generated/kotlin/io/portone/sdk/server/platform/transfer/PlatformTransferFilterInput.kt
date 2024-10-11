package io.portone.sdk.server.platform.transfer

import io.portone.sdk.server.common.PaymentMethodType
import io.portone.sdk.server.platform.DateRange
import io.portone.sdk.server.platform.transfer.PlatformTransferFilterInputKeyword
import io.portone.sdk.server.platform.transfer.PlatformTransferStatus
import io.portone.sdk.server.platform.transfer.PlatformTransferType
import kotlin.Array
import kotlin.String
import kotlinx.serialization.Serializable

/**
 * 정산건 필터 입력 정보
 *
 * 정산 시작일 범위와 정산 일 범위는 둘 중 하나만 입력 가능합니다.
 */
@Serializable
public data class PlatformTransferFilterInput(
  /** 정산 시작일 범위 */
  val settlementStartDateRange: DateRange? = null,
  /** 정산 일 범위 */
  val settlementDateRange: DateRange? = null,
  /**
   * 파트너 태그 리스트
   *
   * 하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 태그를 하나 이상 가지는 파트너에 대한 정산건만 조회합니다.
   */
  val partnerTags: Array<String>? = null,
  /**
   * 계약 아이디 리스트
   *
   * 하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 계약 아이디를 가지는 정산건만 조회합니다.
   */
  val contractIds: Array<String>? = null,
  /**
   * 할인 분담 정책 아이디 리스트
   *
   * 하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 할인 분담 정책 아이디를 하나 이상 가지는 정산건만 조회합니다.
   */
  val discountSharePolicyIds: Array<String>? = null,
  /**
   * 추가 수수료 정책 아이디 리스트
   *
   * 하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 추가 수수료 아이디를 하나 이상 가지는 정산건만 조회합니다.
   */
  val additionalFeePolicyIds: Array<String>? = null,
  /**
   * 결제 수단 리스트
   *
   * 하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 결제 수단을 가지는 파트너만 조회합니다.
   */
  val paymentMethodTypes: Array<PaymentMethodType>? = null,
  /**
   * 채널 키 리스트
   *
   * 하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 채널 키를 가지는 정산건만 조회합니다.
   */
  val channelKeys: Array<String>? = null,
  /**
   * 정산 방식 리스트
   *
   * 하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 정산 방식의 정산건만 조회합니다.
   */
  val types: Array<PlatformTransferType>? = null,
  /**
   * 정산 상태 리스트
   *
   * 하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 정산 상태인 정산건만 조회합니다.
   */
  val statuses: Array<PlatformTransferStatus>? = null,
  /** 검색 키워드 */
  val keyword: PlatformTransferFilterInputKeyword? = null,
  /** 테스트 모드 여부 */
  val isForTest: Boolean? = null,
)
