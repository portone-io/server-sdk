package io.portone.sdk.server.platform.transfer

import kotlin.String
import kotlinx.datetime.Instant
import kotlinx.serialization.Serializable

/** 주문 취소 정보 */
@Serializable
public data class PlatformOrderTransferCancellation(
  /** 주문 취소 아이디 */
  val id: String,
  /** 취소 일시 */
  val cancelledAt: Instant,
)
