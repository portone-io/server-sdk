package io.portone.sdk.server.platform.company

import io.portone.sdk.server.platform.company.B2bBusinessInfo
import kotlin.String
import kotlinx.serialization.Serializable

/** 사업자등록 정보조회 결과 */
@Serializable
public data class B2bBusinessInfoResult(
  /** 사업자등록번호 */
  val brn: String,
  /** 사업자등록 정보 */
  val businessInfo: B2bBusinessInfo? = null,
  /** 조회 실패 시 에러 메시지 */
  val error: String? = null,
  /**
   * 조회 결과 ID
   *
   * 거래처 생성/수정 시 사업자 정보 조회 결과를 재사용하기 위한 ID입니다. 조회 성공 시에만 설정됩니다.
   */
  val verificationId: String? = null,
)


