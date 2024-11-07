package io.portone.sdk.server.payment

import kotlinx.serialization.Serializable

/** 통합검색 항목 */
@Serializable
public enum class PaymentTextSearchField {
  All,
  PaymentId,
  TxId,
  ScheduleId,
  FailReason,
  CardIssuer,
  CardAcquirer,
  CardBin,
  CardNumber,
  CardApprovalNumber,
  CardReceiptName,
  CardInstallment,
  TransBank,
  VirtualAccountHolderName,
  VirtualAccountBank,
  VirtualAccountNumber,
  PgMerchantId,
  PgTxId,
  PgReceiptId,
  ReceiptApprovalNumber,
  PgCancellationId,
  CancelReason,
  OrderName,
  CustomerName,
  CustomerEmail,
  CustomerPhoneNumber,
  CustomerAddress,
  CustomerZipcode,
  UserAgent,
  BillingKey,
  PromotionId,
  GiftCertificationApprovalNumber,
}
