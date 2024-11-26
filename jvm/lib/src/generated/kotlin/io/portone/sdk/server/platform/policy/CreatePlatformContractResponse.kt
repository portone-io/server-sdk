package io.portone.sdk.server.platform.policy

import io.portone.sdk.server.platform.PlatformContract
import kotlinx.serialization.Serializable

/** 계약 객체 생성 성공 응답 */
@Serializable
public data class CreatePlatformContractResponse(
  /** 생성된 계약 객체 */
  val contract: PlatformContract,
)


