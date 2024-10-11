package io.portone.sdk.server.payment

import java.time.Instant
import kotlin.String
import kotlinx.serialization.Serializable

/** 에스크로 배송 정보 등록 성공 응답 */
@Serializable
public data class ApplyEscrowLogisticsResponse(
  /** 송장 번호 */
  val invoiceNumber: String,
  /** 발송 시점 */
  val sentAt: Instant,
  /** 에스크로 정보 등록 시점 */
  val appliedAt: Instant,
)
