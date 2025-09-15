package io.portone.sdk.server.payment

import io.portone.sdk.server.common.Currency
import kotlin.String
import kotlinx.serialization.Serializable

/** 결제 정보 사전 등록 입력 정보 */
@Serializable
internal data class PreRegisterPaymentBody(
  /**
   * 상점 아이디
   *
   * 접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 인증 정보의 상점 아이디를 사용합니다.
   */
  val storeId: String? = null,
  /** 결제 총 금액 */
  val totalAmount: Long? = null,
  /** 결제 면세 금액 */
  val taxFreeAmount: Long? = null,
  /** 통화 단위 */
  val currency: Currency? = null,
)


