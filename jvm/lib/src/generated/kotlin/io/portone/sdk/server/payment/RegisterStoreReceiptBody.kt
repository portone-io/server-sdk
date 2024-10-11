package io.portone.sdk.server.payment

import io.portone.sdk.server.payment.RegisterStoreReceiptBodyItem
import kotlin.String
import kotlinx.serialization.Serializable

/** 영수증 내 하위 상점 거래 등록 정보 */
@Serializable
public data class RegisterStoreReceiptBody(
  /** 하위 상점 거래 목록 */
  val items: List<RegisterStoreReceiptBodyItem>,
  /** 상점 아이디 */
  val storeId: String? = null,
)
