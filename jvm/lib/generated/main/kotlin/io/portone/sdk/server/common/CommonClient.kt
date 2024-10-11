package io.portone.sdk.server

import io.ktor.client.HttpClient
import java.io.Closeable
import kotlinx.serialization.json.Json

public class CommonClient(
  private val apiSecret: String,
  private val storeId: String,
  private val apiBase: String,
) : Closeable {
  private val client: HttpClient = HttpClient(OkHttp)

  private val json: Json = Json { ignoreUnknownKeys = true }
  override fun close() {
    client.close()
  }
}
