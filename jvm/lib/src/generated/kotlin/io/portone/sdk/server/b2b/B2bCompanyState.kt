package io.portone.sdk.server.b2b

import io.portone.sdk.server.b2b.B2bCompanyStateBusinessStatus
import io.portone.sdk.server.b2b.B2bCompanyStateTaxationType
import kotlin.String
import kotlinx.serialization.Serializable

/** 사업자 상태 */
@Serializable
public data class B2bCompanyState(
  /** 사업자 과세 유형 */
  val taxationType: B2bCompanyStateTaxationType,
  /** 사업자 영업 상태 */
  val businessStatus: B2bCompanyStateBusinessStatus,
  /**
   * 과세 유형 변경 일자
   *
   * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
   */
  val taxationTypeDate: String? = null,
  /**
   * 휴폐업 일자
   *
   * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
   */
  val closedSuspendedDate: String? = null,
)
