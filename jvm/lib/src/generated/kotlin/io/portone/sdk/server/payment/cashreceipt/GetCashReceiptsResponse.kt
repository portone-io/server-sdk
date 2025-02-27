package io.portone.sdk.server.payment.cashreceipt

import io.portone.sdk.server.common.PageInfo
import io.portone.sdk.server.payment.cashreceipt.CashReceipt
import kotlinx.serialization.Serializable

/** 현금영수증 다건 조회 성공 응답 정보 */
@Serializable
public data class GetCashReceiptsResponse(
  /** 조회된 현금영수증 리스트 */
  val items: List<CashReceipt>,
  /** 조회된 페이지 정보 */
  val page: PageInfo,
)


