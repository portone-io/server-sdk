package io.portone.sdk.server

import io.ktor.http.URLBuilder
import io.ktor.http.appendPathSegments

internal fun URLBuilder.appendApiPathSegments(vararg segments: String) {
    require(segments.none { it == "." || it == ".." }) { "API path segments cannot be '.' or '..'." }
    appendPathSegments(segments.asList(), encodeSlash = true)
}
