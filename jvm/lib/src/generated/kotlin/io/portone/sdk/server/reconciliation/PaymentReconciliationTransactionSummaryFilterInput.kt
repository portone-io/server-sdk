package io.portone.sdk.server.reconciliation

import io.portone.sdk.server.reconciliation.PaymentReconciliationStatus
import io.portone.sdk.server.reconciliation.ReconciliationPgSpecifier
import kotlin.Array
import kotlin.String
import kotlinx.serialization.Serializable

/** 거래대사 거래내역 필터 */
@Serializable
public data class PaymentReconciliationTransactionSummaryFilterInput(
  /** 대사 상태 필터 */
  val reconciliationStatuses: List<PaymentReconciliationStatus>? = null,
  /** 대사용 PG사 가맹점 식별자 필터 */
  val pgSpecifiers: List<ReconciliationPgSpecifier>? = null,
  /** 하위 상점 아이디 필터 */
  val storeIds: List<String>? = null,
)


