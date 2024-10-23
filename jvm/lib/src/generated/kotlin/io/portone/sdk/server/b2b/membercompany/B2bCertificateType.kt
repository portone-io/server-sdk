package io.portone.sdk.server.b2b.membercompany

import kotlinx.serialization.Serializable

/** 인증서 타입 */
@Serializable
public enum class B2bCertificateType {
  /** 전자세금용 공동인증서 */
  E_TAX,
  /** 특수목적용 공동인증서 */
  PORTONE,
  /** 기타 */
  ETC,
}
