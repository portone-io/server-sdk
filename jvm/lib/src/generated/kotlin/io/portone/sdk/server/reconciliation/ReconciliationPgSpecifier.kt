package io.portone.sdk.server.reconciliation

import io.portone.sdk.server.reconciliation.ReconciliationPgProvider
import kotlin.String
import kotlinx.serialization.Serializable

/** 대사용 PG사 가맹점 식별자 */
@Serializable
public data class ReconciliationPgSpecifier(
  /** PG사 가맹점 식별 아이디 */
  val pgMerchantId: String,
  /** PG사 */
  val pgProvider: ReconciliationPgProvider,
)


