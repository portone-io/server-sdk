package io.portone.sdk.server.b2b

import io.portone.sdk.server.b2b.B2bCertificateType
import kotlin.String
import kotlinx.datetime.Instant
import kotlinx.serialization.Serializable

@Serializable
public data class B2bCertificate(
  /** 등록일시 */
  val registeredAt: Instant,
  /** 만료일시 */
  val expiredAt: Instant,
  /** 발행자명 */
  val issuerDn: String,
  /** 본인명 */
  val subjectDn: String,
  /** 인증서 타입 */
  val certificateType: B2bCertificateType,
  /** OID */
  val oid: String,
  /** 등록 담당자 성명 */
  val registrantContactName: String,
  /** 등록 담당자 ID */
  val registrantContactId: String,
)
