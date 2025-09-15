package io.portone.sdk.server.b2b

import io.ktor.client.HttpClient
import io.ktor.client.engine.okhttp.OkHttp
import io.portone.sdk.server.b2b.taxinvoice.TaxInvoiceClient
import java.io.Closeable
import kotlinx.serialization.json.Json

/**
 * API Secret을 사용해 포트원 API 클라이언트를 생성합니다.
 *
 * @param apiSecret 포트원 API Secret입니다.
 * @param apiBase 포트원 REST API 주소입니다. 기본값은 `"https://api.portone.io"`입니다.
 * @param storeId 하위 상점에 대해 기능을 사용할 때 필요한 하위 상점의 ID입니다.
 */
public class B2bClient(
  private val apiSecret: String,
  private val apiBase: String = "https://api.portone.io",
  private val storeId: String? = null,
): Closeable {
  private val client: HttpClient = HttpClient(OkHttp)

  private val json: Json = Json { ignoreUnknownKeys = true }
  public val taxInvoice: TaxInvoiceClient = TaxInvoiceClient(apiSecret, apiBase, storeId)
  override fun close() {
    taxInvoice.close()
    client.close()
  }
}
