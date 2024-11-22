package io.portone.sdk.server.payment

import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlin.String
import kotlinx.serialization.Serializable

/** 에스크로 배송 정보 수정 성공 응답 */
@Serializable
public data class ModifyEscrowLogisticsResponse(
  /** 송장 번호 */
  val invoiceNumber: String,
  /** 발송 시점 */
  val sentAt: @Serializable(InstantSerializer::class) Instant,
  /** 에스크로 정보 수정 시점 */
  val modifiedAt: @Serializable(InstantSerializer::class) Instant,
)


