package io.portone.sdk.server.payment

import kotlin.String
import kotlinx.serialization.Serializable

/** 수동 매입 입력 정보 */
@Serializable
internal data class CapturePaymentBody(
  /**
   * 상점 아이디
   *
   * 접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 인증 정보의 상점 아이디를 사용합니다.
   */
  val storeId: String? = null,
)


