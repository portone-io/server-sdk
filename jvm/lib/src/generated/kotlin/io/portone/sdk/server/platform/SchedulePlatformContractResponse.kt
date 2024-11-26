package io.portone.sdk.server.platform

import io.portone.sdk.server.platform.PlatformContract
import kotlinx.serialization.Serializable

/** 계약 업데이트 예약 성공 응답 */
@Serializable
public data class SchedulePlatformContractResponse(
  /** 예약된 계약 정보 */
  val scheduledContract: PlatformContract,
)


