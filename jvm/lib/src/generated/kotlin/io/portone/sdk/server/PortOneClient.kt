package io.portone.sdk.server

import io.ktor.client.HttpClient
import io.ktor.client.engine.okhttp.OkHttp
import io.portone.sdk.server.analytics.AnalyticsClient
import io.portone.sdk.server.auth.AuthClient
import io.portone.sdk.server.b2b.B2BClient
import io.portone.sdk.server.identityverification.IdentityVerificationClient
import io.portone.sdk.server.payment.PaymentClient
import io.portone.sdk.server.pgspecific.PgSpecificClient
import io.portone.sdk.server.platform.PlatformClient
import java.io.Closeable
import kotlinx.serialization.json.Json


public class PortOneClient(
  private val apiSecret: String,
  private val storeId: String? = null,
  private val apiBase: String = "https://api.portone.io",
) : Closeable {
  private val client: HttpClient = HttpClient(OkHttp)

  private val json: Json = Json { ignoreUnknownKeys = true }

  public val auth: AuthClient = AuthClient(apiSecret, apiBase, storeId)
  public val platform: PlatformClient = PlatformClient(apiSecret, apiBase, storeId)
  public val identityVerification: IdentityVerificationClient = IdentityVerificationClient(apiSecret, apiBase, storeId)
  public val payment: PaymentClient = PaymentClient(apiSecret, apiBase, storeId)
  public val analytics: AnalyticsClient = AnalyticsClient(apiSecret, apiBase, storeId)
  public val b2b: B2BClient = B2BClient(apiSecret, apiBase, storeId)
  public val pgSpecific: PgSpecificClient = PgSpecificClient(apiSecret, apiBase, storeId)
  override fun close() {
    auth.close()
    platform.close()
    identityVerification.close()
    payment.close()
    analytics.close()
    b2b.close()
    pgSpecific.close()
    client.close()
  }
}
