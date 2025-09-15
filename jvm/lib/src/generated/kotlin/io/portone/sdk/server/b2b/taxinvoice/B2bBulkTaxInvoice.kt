package io.portone.sdk.server.b2b.taxinvoice

import io.portone.sdk.server.b2b.taxinvoice.B2bBulkTaxInvoiceSourceType
import io.portone.sdk.server.b2b.taxinvoice.B2bBulkTaxInvoiceStatus
import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoiceIssuanceType
import io.portone.sdk.server.b2b.taxinvoice.Map_Stat
import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlin.String
import kotlinx.serialization.Serializable

@Serializable
public data class B2bBulkTaxInvoice(
  /** 일괄 세금계산서 고유 아이디 */
  val id: String,
  val graphqlId: String,
  val name: String? = null,
  val status: B2bBulkTaxInvoiceStatus,
  val totalInvoiceCount: Int,
  val totalAmount: Long,
  val stats: Map_Stat,
  val createdAt: @Serializable(InstantSerializer::class) Instant,
  val scheduledAt: @Serializable(InstantSerializer::class) Instant? = null,
  val requestedAt: @Serializable(InstantSerializer::class) Instant? = null,
  val statusUpdatedAt: @Serializable(InstantSerializer::class) Instant,
  val sourceType: B2bBulkTaxInvoiceSourceType,
  val issuanceType: B2bTaxInvoiceIssuanceType,
)


