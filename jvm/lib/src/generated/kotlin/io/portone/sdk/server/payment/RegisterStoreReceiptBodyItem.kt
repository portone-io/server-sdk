package io.portone.sdk.server.payment

import io.portone.sdk.server.common.Currency
import kotlin.String
import kotlinx.serialization.Serializable

/** 하위 상점 거래 정보 */
@Serializable
public data class RegisterStoreReceiptBodyItem(
  /** 하위 상점 사업자등록번호 */
  val storeBusinessRegistrationNumber: String,
  /** 하위 상점명 */
  val storeName: String,
  /** 결제 총 금액 */
  val totalAmount: Long,
  /** 면세액 */
  val taxFreeAmount: Long? = null,
  /** 부가세액 */
  val vatAmount: Long? = null,
  /** 공급가액 */
  val supplyAmount: Long? = null,
  /** 통화 */
  val currency: Currency,
)
