package io.portone.sdk.server.platform.policy

import io.portone.sdk.server.platform.PlatformContract
import kotlinx.serialization.Serializable

/** 계약 보관 성공 응답 */
@Serializable
public data class ArchivePlatformContractResponse(
  /** 보관된 계약 */
  val contract: PlatformContract,
)


