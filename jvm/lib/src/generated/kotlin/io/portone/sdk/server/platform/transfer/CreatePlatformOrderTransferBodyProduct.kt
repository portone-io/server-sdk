package io.portone.sdk.server.platform.transfer

import kotlin.String
import kotlinx.serialization.Serializable

/** 상품 */
@Serializable
public data class CreatePlatformOrderTransferBodyProduct(
  /** 상품 아이디 */
  val id: String,
  /** 상품 이름 */
  val name: String,
  /** 상품 금액 */
  val amount: Long,
  /** 상품 면세 금액 */
  val taxFreeAmount: Long? = null,
  /** 태그 */
  val tag: String? = null,
)
