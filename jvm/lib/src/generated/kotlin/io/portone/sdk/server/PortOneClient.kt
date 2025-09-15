package io.portone.sdk.server

import io.ktor.client.HttpClient
import io.ktor.client.engine.okhttp.OkHttp
import io.ktor.client.plugins.HttpTimeout
import io.portone.sdk.server.auth.AuthClient
import io.portone.sdk.server.b2b.B2bClient
import io.portone.sdk.server.identityverification.IdentityVerificationClient
import io.portone.sdk.server.payment.PaymentClient
import io.portone.sdk.server.pgspecific.PgSpecificClient
import io.portone.sdk.server.platform.PlatformClient
import java.io.Closeable
import kotlinx.serialization.json.Json


/**
 * API Secret을 사용해 포트원 API 클라이언트를 생성합니다.
 *
 * @param apiSecret 포트원 API Secret입니다.
 * @param apiBase 포트원 REST API 주소입니다. 기본값은 `"https://api.portone.io"`입니다.
 * @param storeId 하위 상점에 대해 기능을 사용할 때 필요한 하위 상점의 ID입니다.
 */
public class PortOneClient(
  private val apiSecret: String,
  private val apiBase: String = "https://api.portone.io",
  private val storeId: String? = null,
) : Closeable {
  private val client: HttpClient = HttpClient(OkHttp) {
      install(HttpTimeout) {
          requestTimeoutMillis = 60_000
      }
  }

  private val json: Json = Json { ignoreUnknownKeys = true }

  public val b2b: B2bClient = B2bClient(apiSecret, apiBase, storeId)
  public val platform: PlatformClient = PlatformClient(apiSecret, apiBase, storeId)
  public val payment: PaymentClient = PaymentClient(apiSecret, apiBase, storeId)
  public val identityVerification: IdentityVerificationClient = IdentityVerificationClient(apiSecret, apiBase, storeId)
  public val pgSpecific: PgSpecificClient = PgSpecificClient(apiSecret, apiBase, storeId)
  public val auth: AuthClient = AuthClient(apiSecret, apiBase, storeId)
  override fun close() {
    b2b.close()
    platform.close()
    payment.close()
    identityVerification.close()
    pgSpecific.close()
    auth.close()
    client.close()
  }
}
