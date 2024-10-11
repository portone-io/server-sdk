package io.portone.sdk.server.webhook

/**
 * Thrown to indicate that the webhook verification failed.
 */
public class WebhookVerificationException internal constructor(message: String, cause: Throwable? = null) : Exception(message, cause) {
    public companion object {
        @Suppress("ConstPropertyName")
        private const val serialVersionUID: Long = 6521886437375683450L
    }
}
