package io.portone.sdk.server.webhook

import java.security.MessageDigest
import java.util.Base64
import javax.crypto.Mac
import javax.crypto.spec.SecretKeySpec

/**
 * Verifies webhook messages as specified in [Standard Webhooks](https://www.standardwebhooks.com/).
 *
 * The implementation is based on [the reference implementation](https://github.com/standard-webhooks/standard-webhooks/tree/main/libraries/java).
 *
 * Only supports symmetric signatures based on HMAC-SHA256.
 *
 * An instance of `WebhookVerifier` is an immutable object holding the secret key. It is safe to share the instance between invocations and threads.
 *
 * Example:
 * ```kotlin
 * import io.portone.sdk.server.webhook.WebhookVerifier
 *
 * // The webhook secret can be issued from the PortOne admin console.
 * // This is different from the API secret.
 * val webhookVerifier = WebhookVerifier("YOUR_WEBHOOK_SECRET_HERE")
 *
 * // on each request
 * try {
 *     webhookVerifier.verify(
 *         payload = body,
 *         msgId = headers[WebhookVerifier.HEADER_ID],
 *         msgSignature = headers[WebhookVerifier.HEADER_SIGNATURE],
 *         msgTimestamp = headers[webhookVerifier.HEADER_TIMESTAMP],
 *     )
 * } catch (e: WebhookVerificationException) {
 *     // verification failed. log e.message and ignore the request.
 * }
 * ```
 */
public class WebhookVerifier private constructor(private val secretKeySpec: SecretKeySpec) {
    /**
     * Constructs the verifier with the secret key.
     *
     * @param secretKey the secret key. should not be empty.
     */
    public constructor(secretKey: ByteArray) : this(SecretKeySpec(secretKey, HMAC_SHA256))

    /**
     * Constructs the verifier with the secret key encoded in Base64.
     *
     * If the secret key starts with the prefix "whsec_", the prefix is ignored.
     *
     * @param secretKey the secret key. Should be an optionally prefixed valid Base64 string which decodes to non-empty bytes.
     */
    public constructor(secretKey: String) : this(
        Base64.getDecoder().decode(
            if (secretKey.startsWith(SECRET_PREFIX)) secretKey.substring(SECRET_PREFIX.length) else secretKey,
        ),
    )

    /**
     * Verifies a webhook message. When the verification fails, throws [WebhookVerificationException].
     *
     * If the verification fails, the caller should not trust the request. It is recommended to simply log the failure and ignore the request.
     *
     * msgId, msgSignature and msgTimestamp are declared nullable for convenience. If any of the parameters are null, the verification fails.
     *
     * @param msgBody the body of the request.
     * @param msgId the value of the header whose name equals [HEADER_ID].
     * @param msgSignature the value of the header whose name equals [HEADER_SIGNATURE].
     * @param msgTimestamp the value of the header whose name equals [HEADER_TIMESTAMP].
     *
     * @throws WebhookVerificationException when the verification fails.
     */
    @Throws(WebhookVerificationException::class)
    public fun verify(
        msgBody: String,
        msgId: String?,
        msgSignature: String?,
        msgTimestamp: String?,
    ) {
        if (msgId == null || msgSignature == null || msgTimestamp == null) {
            throw WebhookVerificationException("Missing required headers")
        }

        val timestamp = verifyTimestamp(msgTimestamp)

        val expectedSignature = sign(msgId, timestamp, msgBody)

        val msgSignatures = msgSignature.splitToSequence(' ')
        if (msgSignatures.none { versionedSignature ->
                val sigParts = versionedSignature.split(',', limit = 3) // ignore after the second comma
                if (sigParts.size < 2) return@none false
                val (version, signatureStr) = sigParts

                if (version != "v1") return@none false

                val signature =
                    try {
                        Base64.getDecoder().decode(signatureStr)
                    } catch (e: IllegalArgumentException) {
                        return@none false
                    }

                MessageDigest.isEqual(signature, expectedSignature)
            }
        ) {
            throw WebhookVerificationException("No matching signature found")
        }
    }

    private fun sign(
        msgId: String?,
        timestamp: Long,
        payload: String,
    ): ByteArray {
        val mac = Mac.getInstance(HMAC_SHA256)
        mac.init(secretKeySpec)
        return mac.doFinal("$msgId.$timestamp.$payload".toByteArray())
    }

    public companion object {
        /**
         * The name of the HTTP header for the message id.
         */
        public const val HEADER_ID: String = "webhook-id"

        /**
         * The name of the HTTP header for the message signature.
         */
        public const val HEADER_SIGNATURE: String = "webhook-signature"

        /**
         * The name of the HTTP header for the message timestamp.
         */
        public const val HEADER_TIMESTAMP: String = "webhook-timestamp"

        private const val SECRET_PREFIX: String = "whsec_"
        private const val HMAC_SHA256 = "HmacSHA256"
        private const val TOLERANCE_IN_SECONDS = 5 * 60 // 5 minutes
        private const val SECOND_IN_MS = 1000L

        @Throws(WebhookVerificationException::class)
        private fun verifyTimestamp(msgTimestamp: String): Long {
            val now = System.currentTimeMillis() / SECOND_IN_MS

            val timestamp = msgTimestamp.toLongOrNull() ?: throw WebhookVerificationException("Invalid Signature Headers")

            if (timestamp < (now - TOLERANCE_IN_SECONDS)) {
                throw WebhookVerificationException("Message timestamp too old")
            }
            if (timestamp > (now + TOLERANCE_IN_SECONDS)) {
                throw WebhookVerificationException("Message timestamp too new")
            }
            return timestamp
        }
    }
}
