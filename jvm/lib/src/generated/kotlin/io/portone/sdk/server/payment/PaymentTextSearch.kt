package io.portone.sdk.server.payment

import io.portone.sdk.server.payment.PaymentTextSearchField
import kotlin.String
import kotlinx.serialization.Serializable

/** 통합검색 입력 정보 */
@Serializable
public data class PaymentTextSearch(
  val field: PaymentTextSearchField,
  val value: String,
)


