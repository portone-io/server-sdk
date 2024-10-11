package io.portone.sdk.server.b2b

import kotlinx.serialization.Serializable

/** 인증서 타입 */
@Serializable
public enum class B2bCertificateType {
  /** 전자세금용 공동인증서 */
  E_TAX,
  /** 팝빌 특목용 공동인증서 */
  POP_BILL,
  /** 기타 */
  ETC,
}
