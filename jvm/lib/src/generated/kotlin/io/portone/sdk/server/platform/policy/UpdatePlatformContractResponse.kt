package io.portone.sdk.server.platform.policy

import io.portone.sdk.server.platform.PlatformContract
import kotlinx.serialization.Serializable

/** 계약 객체 업데이트 성공 응답 */
@Serializable
public data class UpdatePlatformContractResponse(
  /** 업데이트된 계약 객체 */
  val contract: PlatformContract,
)


