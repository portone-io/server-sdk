package io.portone.sdk.server.platform

import kotlin.String
import kotlinx.serialization.Serializable

/** 플랫폼 설정 */
@Serializable
public data class PlatformSetting(
  /** 기본 보내는 이 통장 메모 */
  val defaultWithdrawalMemo: String? = null,
  /** 기본 받는 이 통장 메모 */
  val defaultDepositMemo: String? = null,
)


