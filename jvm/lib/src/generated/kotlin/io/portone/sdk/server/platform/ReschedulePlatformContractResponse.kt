package io.portone.sdk.server.platform

import io.portone.sdk.server.platform.PlatformContract
import kotlinx.serialization.Serializable

/** 계약 예약 업데이트 재설정 성공 응답 */
@Serializable
public data class ReschedulePlatformContractResponse(
  /** 예약된 계약 정보 */
  val scheduledContract: PlatformContract,
)
