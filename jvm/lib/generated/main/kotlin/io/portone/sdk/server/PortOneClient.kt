package io.portone.sdk.server

import io.ktor.client.HttpClient
import io.portone.sdk.server.analytics.AnalyticsClient
import io.portone.sdk.server.auth.AuthClient
import io.portone.sdk.server.b2b.B2BClient
import io.portone.sdk.server.billingkey.BillingKeyClient
import io.portone.sdk.server.cashreceipt.CashReceiptClient
import io.portone.sdk.server.common.CommonClient
import io.portone.sdk.server.identityverification.IdentityVerificationClient
import io.portone.sdk.server.payment.PaymentClient
import io.portone.sdk.server.paymentschedule.PaymentScheduleClient
import io.portone.sdk.server.pgspecific.PgSpecificClient
import io.portone.sdk.server.platform.PlatformClient
import io.portone.sdk.server.promotion.PromotionClient
import java.io.Closeable
import kotlinx.serialization.json.Json


public class PortOneClient(
  private val apiSecret: String,
  private val storeId: String? = null,
  private val apiBase: String = "https://api.portone.io",
) : Closeable {
  private val client: HttpClient = HttpClient(OkHttp)

  private val json: Json = Json { ignoreUnknownKeys = true }

  public val auth: AuthClient = AuthClient(apiSecret, storeId, apiBase)
  public val platform: PlatformClient = PlatformClient(apiSecret, storeId, apiBase)
  public val identityVerification: IdentityVerificationClient = IdentityVerificationClient(apiSecret, storeId, apiBase)
  public val payment: PaymentClient = PaymentClient(apiSecret, storeId, apiBase)
  public val billingKey: BillingKeyClient = BillingKeyClient(apiSecret, storeId, apiBase)
  public val cashReceipt: CashReceiptClient = CashReceiptClient(apiSecret, storeId, apiBase)
  public val paymentSchedule: PaymentScheduleClient = PaymentScheduleClient(apiSecret, storeId, apiBase)
  public val analytics: AnalyticsClient = AnalyticsClient(apiSecret, storeId, apiBase)
  public val b2b: B2BClient = B2BClient(apiSecret, storeId, apiBase)
  public val pgSpecific: PgSpecificClient = PgSpecificClient(apiSecret, storeId, apiBase)
  public val promotion: PromotionClient = PromotionClient(apiSecret, storeId, apiBase)
  public val common: CommonClient = CommonClient(apiSecret, storeId, apiBase)
  override fun close() {
    auth.close()
    platform.close()
    identityVerification.close()
    payment.close()
    billingKey.close()
    cashReceipt.close()
    paymentSchedule.close()
    analytics.close()
    b2b.close()
    pgSpecific.close()
    promotion.close()
    common.close()
    client.close()
  }
}
