package io.portone.sdk.server.platform.account

import kotlin.String
import kotlinx.serialization.Serializable

/** 예금주 조회 성공 응답 정보 */
@Serializable
public data class PlatformAccountHolder(
  /** 계좌 예금주 이름 */
  val holderName: String,
  /** 계좌 검증 아이디 */
  val accountVerificationId: String,
)


