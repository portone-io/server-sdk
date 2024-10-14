package io.portone.sdk.server.payment.billingkey

import io.portone.sdk.server.payment.billingkey.BillingKeyTextSearchField
import kotlin.String
import kotlinx.serialization.Serializable

/** 통합검색 입력 정보 */
@Serializable
public data class BillingKeyTextSearch(
  val field: BillingKeyTextSearchField,
  val value: String,
)
