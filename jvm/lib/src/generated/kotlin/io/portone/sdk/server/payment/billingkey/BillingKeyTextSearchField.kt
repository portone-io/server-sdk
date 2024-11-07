package io.portone.sdk.server.payment.billingkey

import kotlinx.serialization.Serializable

/** 통합검색 항목 */
@Serializable
public enum class BillingKeyTextSearchField {
  CardBin,
  CardNumber,
  PgMerchantId,
  CustomerName,
  CustomerEmail,
  CustomerPhoneNumber,
  CustomerAddress,
  CustomerZipcode,
  UserAgent,
  BillingKey,
  ChannelGroupName,
}
