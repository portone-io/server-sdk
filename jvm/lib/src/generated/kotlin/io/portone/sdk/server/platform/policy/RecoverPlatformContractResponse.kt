package io.portone.sdk.server.platform.policy

import io.portone.sdk.server.platform.PlatformContract
import kotlinx.serialization.Serializable

/** 계약 복원 성공 응답 */
@Serializable
public data class RecoverPlatformContractResponse(
  /** 복원된 계약 */
  val contract: PlatformContract,
)
