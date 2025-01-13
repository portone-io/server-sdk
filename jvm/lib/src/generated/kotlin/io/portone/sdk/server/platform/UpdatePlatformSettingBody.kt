package io.portone.sdk.server.platform

import kotlin.String
import kotlinx.serialization.Serializable

/** 플랫폼 설정 업데이트를 위한 입력 정보 */
@Serializable
internal data class UpdatePlatformSettingBody(
  /** 기본 보내는 이 통장 메모 */
  val defaultWithdrawalMemo: String? = null,
  /** 기본 받는 이 통장 메모 */
  val defaultDepositMemo: String? = null,
)


