package io.portone.sdk.server.common

import io.ktor.client.HttpClient
import io.ktor.client.engine.okhttp.OkHttp
import java.io.Closeable
import kotlinx.serialization.json.Json

public class CommonClient(
  private val apiSecret: String,
  private val apiBase: String,
  private val storeId: String?,
) : Closeable {
  private val client: HttpClient = HttpClient(OkHttp)

  private val json: Json = Json { ignoreUnknownKeys = true }
  override fun close() {
    client.close()
  }
}
