package io.portone.sdk.server.identityverification

import kotlinx.serialization.Serializable

/** 본인인증 통신사 */
@Serializable
public enum class IdentityVerificationOperator {
  /** SKT */
  Skt,
  /** KT */
  Kt,
  /** LGU */
  Lgu,
  /** SKT 알뜰폰 */
  SktMvno,
  /** KT 알뜰폰 */
  KtMvno,
  /** LGU 알뜰폰 */
  LguMvno,
}
