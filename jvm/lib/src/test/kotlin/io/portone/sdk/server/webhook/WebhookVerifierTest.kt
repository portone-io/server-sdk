package io.portone.sdk.server.webhook

import kotlinx.serialization.encodeToString
import kotlinx.serialization.json.Json
import java.time.Instant
import javax.crypto.Mac
import javax.crypto.spec.SecretKeySpec
import kotlin.io.encoding.Base64
import kotlin.io.encoding.ExperimentalEncodingApi
import kotlin.test.Test
import kotlin.test.assertEquals

class WebhookVerifierTest {
    companion object {
        private const val HMAC_SHA256 = "HmacSHA256"
    }

    @OptIn(ExperimentalEncodingApi::class)
    private val secret = Base64.decode("pzQGE83cSIRKM4/WH5QY+g==")
    private val verifier = WebhookVerifier(secret)
    private val json = Json

    private val testObjectUnrecognized = json.encodeToString(mapOf("test" to "test payload"))
    private val testObjectRecognized =
        json.encodeToString(
            mapOf(
                "type" to "Transaction.Cancelled",
                "timestamp" to "2024-04-25T10:00:00.000Z",
                "data" to
                    mapOf(
                        "paymentId" to "example-payment-id",
                        "transactionId" to "55451513-9763-4a7a-bb43-78a4c65be843",
                        "cancellationId" to "0cdd91e9-4e7c-44a3-a72e-1a6511826c2b",
                    ),
            ),
        )

    data class WebhookMock(
        val payload: String,
        val id: String,
        val signature: String,
        val timestamp: String,
    )

    @OptIn(ExperimentalEncodingApi::class)
    private fun makeWebhook(
        body: String,
        epochSecond: Long = Instant.now().epochSecond,
    ): WebhookMock {
        val id = "dummy-webhook-id"
        val plaintext = "$id.$epochSecond.$body".toByteArray()
        val hmac = Mac.getInstance(HMAC_SHA256).apply { init(SecretKeySpec(secret, HMAC_SHA256)) }
        val signature = hmac.doFinal(plaintext)
        val payload = Base64.encode(signature)
        return WebhookMock(
            payload,
            id,
            "v1,$payload",
            epochSecond.toString(),
        )
    }

    @Test
    fun testVerifyValidSignatureUnrecognized() {
        val mock = makeWebhook(testObjectUnrecognized)
        val webhook = verifier.verify(mock.payload, mock.id, mock.signature, mock.timestamp)
        assertEquals(webhook, Webhook.Unrecognized)
    }

    @Test
    fun testVerifyValidSignatureRecognized() {
        val mock = makeWebhook(testObjectRecognized)
        val webhook = verifier.verify(mock.payload, mock.id, mock.signature, mock.timestamp)
        assertEquals(
            webhook,
            WebhookTransactionCancelledCancelled(
                timestamp = Instant.parse("2024-04-25T10:00:00.000Z"),
                data =
                    WebhookTransactionCancelledDataCancelled(
                        paymentId = "example-payment-id",
                        transactionId = "55451513-9763-4a7a-bb43-78a4c65be843",
                        cancellationId = "0cdd91e9-4e7c-44a3-a72e-1a6511826c2b",
                    ),
            ),
        )
    }
}
