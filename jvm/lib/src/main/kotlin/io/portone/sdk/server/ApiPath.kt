package io.portone.sdk.server

import io.ktor.http.URLBuilder
import io.ktor.http.appendPathSegments

private val dotSegment = Regex("""(?:\.|%2[eE]){1,2}""")

internal fun URLBuilder.appendApiPathSegments(vararg segments: String) {
    require(segments.none(dotSegment::matches)) { "API path segments cannot be '.' or '..', including percent-encoded forms." }
    appendPathSegments(segments.asList(), encodeSlash = true)
}
