package io.portone.sdk.server.payment.billingkey

import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlin.String
import kotlinx.serialization.Serializable

/** 발급 실패 상세 정보 */
@Serializable
public data class BillingKeyFailure(
  /** 실패 사유 */
  val message: String? = null,
  /** PG사 실패 코드 */
  val pgCode: String? = null,
  /** PG사 실패 사유 */
  val pgMessage: String? = null,
  /** 실패 시점 */
  val failedAt: @Serializable(InstantSerializer::class) Instant,
)


