package io.portone.sdk.server.payment

import io.portone.sdk.server.common.PageInfo
import io.portone.sdk.server.payment.Payment
import kotlinx.serialization.Serializable

/** 결제 건 다건 조회 성공 응답 정보 */
@Serializable
public data class GetPaymentsResponse(
  /** 조회된 결제 건 리스트 */
  val items: Array<Payment>,
  /** 조회된 페이지 정보 */
  val page: PageInfo,
)
