package io.portone.sdk.server.b2b.membercompany

import io.portone.sdk.server.b2b.membercompany.B2bCertificateType
import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlin.String
import kotlinx.serialization.Serializable

@Serializable
public data class B2bCertificate(
  /** 등록일시 */
  val registeredAt: @Serializable(InstantSerializer::class) Instant,
  /** 만료일시 */
  val expiredAt: @Serializable(InstantSerializer::class) Instant,
  /** 발행자명 */
  val issuerName: String,
  /** 본인명 */
  val subjectName: String,
  /** 인증서 타입 */
  val certificateType: B2bCertificateType,
  /** OID */
  val oid: String,
  /** 등록 담당자 성명 */
  val registrantContactName: String,
  /** 등록 담당자 ID */
  val registrantContactId: String,
)
