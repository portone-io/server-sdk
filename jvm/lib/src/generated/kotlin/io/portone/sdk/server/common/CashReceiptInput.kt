package io.portone.sdk.server.common

import io.portone.sdk.server.common.CashReceiptInputType
import kotlin.String
import kotlinx.serialization.Serializable

/** 현금영수증 입력 정보 */
@Serializable
public data class CashReceiptInput(
  /** 현금영수증 유형 */
  val type: CashReceiptInputType,
  /**
   * 사용자 식별 번호
   *
   * 미발행 유형 선택 시 입력하지 않습니다.
   */
  val customerIdentityNumber: String? = null,
)
