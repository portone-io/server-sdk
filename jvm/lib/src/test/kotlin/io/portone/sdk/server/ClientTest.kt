package io.portone.sdk.server

import com.sun.net.httpserver.Headers
import com.sun.net.httpserver.HttpServer
import io.portone.sdk.server.common.PageInput
import io.portone.sdk.server.errors.PaymentAlreadyCancelledException
import io.portone.sdk.server.errors.PaymentNotFoundException
import io.portone.sdk.server.payment.CancelledPayment
import io.portone.sdk.server.payment.GetPaymentsResponse
import io.portone.sdk.server.payment.PaymentClient
import kotlinx.coroutines.test.runTest
import kotlinx.serialization.json.Json
import org.junit.jupiter.api.assertThrows
import java.net.InetSocketAddress
import java.net.URLDecoder
import java.util.concurrent.ArrayBlockingQueue
import kotlin.test.AfterTest
import kotlin.test.BeforeTest
import kotlin.test.Test
import kotlin.test.assertContentEquals
import kotlin.test.assertEquals
import kotlin.test.assertIs
import kotlin.test.assertTrue

class ClientTest {
    private data class Request(
        val method: String,
        val path: String,
        val query: String?,
        val headers: Headers,
        val body: String,
    )

    private lateinit var server: HttpServer
    private lateinit var client: PaymentClient
    private val requests = ArrayBlockingQueue<Request>(1)
    private var status = 200
    private var response = """{"items":[],"page":{"number":0,"size":0,"totalCount":0}}"""

    @BeforeTest
    fun setUp() {
        server = HttpServer.create(InetSocketAddress("127.0.0.1", 0), 0)
        server.createContext("/") { exchange ->
            requests.add(
                Request(
                    exchange.requestMethod,
                    exchange.requestURI.rawPath,
                    exchange.requestURI.rawQuery,
                    exchange.requestHeaders,
                    exchange.requestBody.bufferedReader().readText(),
                ),
            )
            val bytes = response.toByteArray(Charsets.UTF_8)
            exchange.responseHeaders.add("Content-Type", "application/json")
            exchange.sendResponseHeaders(status, bytes.size.toLong())
            exchange.responseBody.use { it.write(bytes) }
        }
        server.start()
        client = PaymentClient(apiSecret = "test-secret", apiBase = "http://127.0.0.1:${server.address.port}")
    }

    @AfterTest
    fun tearDown() {
        client.close()
        server.stop(0)
    }

    private fun assertRequest(
        method: String,
        path: String,
        query: String? = null,
        body: String? = null,
    ) {
        val request = requests.remove()
        assertEquals(method, request.method)
        assertEquals(path, request.path)
        if (query?.startsWith("requestBody=") == true) {
            val decoded = URLDecoder.decode(checkNotNull(request.query), "UTF-8")
            assertTrue(decoded.startsWith("requestBody="))
            assertEquals(
                Json.parseToJsonElement(query.removePrefix("requestBody=")),
                Json.parseToJsonElement(decoded.removePrefix("requestBody=")),
            )
        } else {
            assertEquals(query, request.query)
        }
        if (body ==
            null
        ) {
            assertEquals("", request.body)
        } else {
            assertEquals(Json.parseToJsonElement(body), Json.parseToJsonElement(request.body))
        }
        assertEquals("PortOne test-secret", request.headers.getFirst("Authorization"))
        assertTrue(!request.headers.getFirst("User-Agent").isNullOrBlank())
    }

    @Test
    fun testGetPaymentsWithoutParams() =
        runTest {
            assertIs<GetPaymentsResponse>(client.getPayments())
            assertRequest("GET", "/payments", "requestBody={}")
        }

    @Test
    fun testGetPaymentsWithParams() =
        runTest {
            val payments = client.getPayments(PageInput(3000))
            assertContentEquals(emptyList(), payments.items)
            assertRequest("GET", "/payments", "requestBody={\"page\":{\"number\":3000}}")
        }

    @Test
    fun testGetPaymentWithParams() =
        runTest {
            response =
                """{"status":"CANCELLED","id":"test-server-sdk","transactionId":"tx-1","merchantId":"merchant-1","storeId":"store-1","channel":{"type":"TEST","pgProvider":"KCP","pgMerchantId":"pg-1"},"version":"V2","requestedAt":"2024-01-01T00:00:00Z","updatedAt":"2024-01-01T00:00:00Z","statusChangedAt":"2024-01-01T00:00:00Z","orderName":"Test order","amount":{"total":100,"taxFree":0,"discount":0,"paid":100,"cancelled":100,"cancelledTaxFree":0},"currency":"KRW","customer":{},"origin":{"platformType":"API","ipAddress":"127.0.0.1"},"cancellations":[],"cancelledAt":"2024-01-01T00:00:00Z"}"""
            val payment = assertIs<CancelledPayment>(client.getPayment("test-server-sdk"))
            assertEquals("test-server-sdk", payment.id)
            assertEquals("Test order", payment.orderName)
            assertEquals(100L, payment.amount.cancelled)
            assertRequest("GET", "/payments/test-server-sdk")
        }

    @Test
    fun testGetPaymentEncodesPaymentId() =
        runTest {
            status = 404
            response = """{"type":"PAYMENT_NOT_FOUND","message":"Payment not found"}"""
            for ((id, encoded) in listOf(" " to "%20", "order.v2/part" to "order.v2%2Fpart", "..." to "...")) {
                assertThrows<PaymentNotFoundException> { client.getPayment(id) }
                assertRequest("GET", "/payments/$encoded")
            }
        }

    @Test
    fun testGetPaymentRejectsDotSegmentsBeforeSending() =
        runTest {
            val dots = listOf(".", "%2e", "%2E")
            val dotSegments = dots + dots.flatMap { first -> dots.map { second -> first + second } }
            for (id in dotSegments) {
                assertThrows<IllegalArgumentException> { client.getPayment(id) }
            }
            assertTrue(requests.isEmpty())
        }

    @Test
    fun testCancelPaymentWithAlreadyCancelledPaymentId() =
        runTest {
            status = 409
            response = """{"type":"PAYMENT_ALREADY_CANCELLED","message":"Already cancelled"}"""
            assertThrows<PaymentAlreadyCancelledException> {
                client.cancelPayment(
                    paymentId = "test-server-sdk",
                    reason = "test",
                    amount = 1,
                )
            }
            assertRequest("POST", "/payments/test-server-sdk/cancel", body = """{"amount":1,"reason":"test"}""")
        }

    @Test
    fun testStoreId() =
        runTest {
            client.close()
            client = PaymentClient(apiSecret = "test-secret", apiBase = "http://127.0.0.1:${server.address.port}", storeId = "store-1")
            status = 404
            response = """{"type":"PAYMENT_NOT_FOUND","message":"Payment not found"}"""
            assertThrows<PaymentNotFoundException> { client.getPayment("test-server-sdk") }
            assertRequest("GET", "/payments/test-server-sdk", "storeId=store-1")
        }
}
