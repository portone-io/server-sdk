package io.portone.sdk.server.billingkey

import kotlinx.datetime.Instant
import kotlinx.serialization.Serializable

/** 빌링키 삭제 성공 응답 */
@Serializable
public data class DeleteBillingKeyResponse(
  /** 빌링키 삭제 완료 시점 */
  val deletedAt: Instant,
)
