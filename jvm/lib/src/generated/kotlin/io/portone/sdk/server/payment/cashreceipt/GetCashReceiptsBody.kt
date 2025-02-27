package io.portone.sdk.server.payment.cashreceipt

import io.portone.sdk.server.common.PageInput
import io.portone.sdk.server.payment.cashreceipt.CashReceiptFilterInput
import io.portone.sdk.server.payment.cashreceipt.CashReceiptSortInput
import kotlinx.serialization.Serializable

/** 현금영수증 다건 조회를 위한 입력 정보 */
@Serializable
internal data class GetCashReceiptsBody(
  /**
   * 요청할 페이지 정보
   *
   * 미 입력 시 number: 0, size: 10 으로 기본값이 적용됩니다.
   */
  val page: PageInput? = null,
  /**
   * 정렬 조건
   *
   * 미 입력 시 sortBy: ISSUED_AT, sortOrder: DESC 으로 기본값이 적용됩니다.
   */
  val sort: CashReceiptSortInput? = null,
  /** 조회할 현금영수증 조건 필터 */
  val filter: CashReceiptFilterInput? = null,
)


