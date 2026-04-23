package io.portone.sdk.server.b2b.counterparty

import io.portone.sdk.server.b2b.counterparty.B2bCounterpartyBusinessStatus
import io.portone.sdk.server.b2b.counterparty.B2bNtsConnectionStatus
import kotlin.Array
import kotlin.String
import kotlinx.serialization.Serializable

/** 거래처 검색 필터 */
@Serializable
public data class B2bCounterpartyFilter(
  /**
   * 거래처 ID
   *
   * prefix 검색
   */
  val id: String? = null,
  /** 사업자등록번호 */
  val brn: String? = null,
  /**
   * 거래처명
   *
   * 포함 검색
   */
  val companyName: String? = null,
  /** 대표자명 */
  val representativeName: String? = null,
  /** 담당자 이름 */
  val contactName: String? = null,
  /** 담당자 전화번호 */
  val contactPhone: String? = null,
  /** 담당자 이메일 */
  val contactEmail: String? = null,
  /** 휴폐업 상태 */
  val businessStatuses: List<B2bCounterpartyBusinessStatus>? = null,
  /** 국세청 연동 상태 */
  val ntsConnectionStatuses: List<B2bNtsConnectionStatus>? = null,
  /**
   * 거래처 ID 목록
   *
   * 특정 ID 목록으로 필터링
   */
  val counterpartyIds: List<String>? = null,
)


