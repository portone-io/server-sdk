package io.portone.sdk.server.common

import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlin.String
import kotlinx.serialization.Serializable

/** 담당자 정보 */
@Serializable
public data class B2bCompanyContact(
  /**
   * 담당자 계정 ID
   *
   * 팝빌 로그인 계정으로 사용됩니다.
   */
  val loginId: String,
  /** 담당자 성명 */
  val name: String,
  /** 담당자 핸드폰 번호 */
  val phoneNumber: String,
  /** 담당자 이메일 */
  val email: String,
  /** 등록 일시 */
  val registeredAt: @Serializable(InstantSerializer::class) Instant,
  /**
   * 관리자 여부
   *
   * true일 경우 관리자 권한, false일 경우 일반 권한 담당자입니다.
   */
  val isAdmin: Boolean,
)
