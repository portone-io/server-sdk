package io.portone.sdk.server.identityverification

import kotlin.String
import kotlinx.serialization.Serializable

/** 본인인증 실패 정보 */
@Serializable
public data class IdentityVerificationFailure(
  /** 실패 사유 */
  val reason: String? = null,
  /** PG사 실패 코드 */
  val pgCode: String? = null,
  /** PG사 실패 메시지 */
  val pgMessage: String? = null,
)
