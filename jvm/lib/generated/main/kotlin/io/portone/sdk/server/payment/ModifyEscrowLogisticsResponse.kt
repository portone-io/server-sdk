package io.portone.sdk.server.payment

import kotlin.String
import kotlinx.datetime.Instant
import kotlinx.serialization.Serializable

/** 에스크로 배송 정보 수정 성공 응답 */
@Serializable
public data class ModifyEscrowLogisticsResponse(
  /** 송장 번호 */
  val invoiceNumber: String,
  /** 발송 시점 */
  val sentAt: Instant,
  /** 에스크로 정보 수정 시점 */
  val modifiedAt: Instant,
)
