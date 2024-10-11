package io.portone.sdk.server.platform.transfer

import java.time.Instant
import kotlinx.serialization.Serializable

/** 외부 결제 상세 정보 */
@Serializable
public data class CreatePlatformOrderCancelTransferBodyExternalCancellationDetail(
  /** 취소 일시 */
  val cancelledAt: Instant? = null,
)
