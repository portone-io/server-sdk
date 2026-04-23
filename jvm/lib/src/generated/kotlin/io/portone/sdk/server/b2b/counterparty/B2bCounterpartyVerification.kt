package io.portone.sdk.server.b2b.counterparty

import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlin.String
import kotlinx.serialization.Serializable

/** 거래처 검증 정보 */
@Serializable
public data class B2bCounterpartyVerification(
  /** 외부 API 사용 ID */
  val id: String,
  /** 검증 시각 */
  val checkedAt: @Serializable(InstantSerializer::class) Instant,
)


