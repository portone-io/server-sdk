package io.portone.sdk.server.errors

/**
 * API 응답이 알 수 없는 형식임을 나타냅니다.
 */
public class UnknownException internal constructor(message: String, cause: Throwable? = null) : Exception(message, cause) {
    public companion object {
        @Suppress("ConstPropertyName")
        private const val serialVersionUID: Long = 788381635814915564L
    }
}
