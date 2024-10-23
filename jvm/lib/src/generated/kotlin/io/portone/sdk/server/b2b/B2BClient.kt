package io.portone.sdk.server.b2b

import io.ktor.client.HttpClient
import io.ktor.client.engine.okhttp.OkHttp
import io.portone.sdk.server.b2b.contact.ContactClient
import io.portone.sdk.server.b2b.membercompany.MemberCompanyClient
import io.portone.sdk.server.b2b.taxinvoice.TaxInvoiceClient
import java.io.Closeable
import kotlinx.serialization.json.Json

public class B2BClient internal constructor(
  private val apiSecret: String,
  private val apiBase: String,
  private val storeId: String?,
) {
  private val client: HttpClient = HttpClient(OkHttp)

  private val json: Json = Json { ignoreUnknownKeys = true }
  public val MemberCompany: MemberCompanyClient = MemberCompanyClient(apiSecret, apiBase, storeId)
  public val Contact: ContactClient = ContactClient(apiSecret, apiBase, storeId)
  public val TaxInvoice: TaxInvoiceClient = TaxInvoiceClient(apiSecret, apiBase, storeId)
  internal fun close() {
    MemberCompany.close()
    Contact.close()
    TaxInvoice.close()
    client.close()
  }
}
