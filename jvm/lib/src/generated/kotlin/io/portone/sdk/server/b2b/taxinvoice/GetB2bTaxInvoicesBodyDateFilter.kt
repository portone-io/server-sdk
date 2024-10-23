package io.portone.sdk.server.b2b.taxinvoice

import io.portone.sdk.server.b2b.taxinvoice.B2bSearchDateType
import io.portone.sdk.server.b2b.taxinvoice.DateRangeOption
import kotlinx.serialization.Serializable

/** 조회 기간 필터 */
@Serializable
public data class GetB2bTaxInvoicesBodyDateFilter(
  /**
   * 조회 기간 기준
   *
   * 미입력시 기본값은 등록일(`REGISTER`)로 설정됩니다.
   */
  val dateType: B2bSearchDateType? = null,
  /**
   * 조회 기간
   *
   * 미입력시 `dateRange.from`의 기본값은 한 달 이전, `dateRange.until`의 기본값은 현재 일자로 설정됩니다.
   */
  val dateRange: List<DateRangeOption>? = null,
)
