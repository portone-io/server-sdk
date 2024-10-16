package io.portone.sdk.server.analytics

import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlinx.serialization.Serializable

/** 고객사의 PG사별 결제전환율 조회를 위한 입력 정보 */
@Serializable
internal data class GetAnalyticsPaymentStatusByPgCompanyChartBody(
  /** 조회할 결제 현황의 시작 시간 */
  val `from`: @Serializable(InstantSerializer::class) Instant,
  /** 조회할 결제 현황의 끝 시간 */
  val until: @Serializable(InstantSerializer::class) Instant,
  /**
   * 조회할 결제 통화
   *
   * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
   */
  val currency: Currency,
)
