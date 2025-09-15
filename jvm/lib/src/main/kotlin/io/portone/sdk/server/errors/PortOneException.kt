package io.portone.sdk.server.errors

public sealed class PortOneException(
    override val message: String?,
    override val cause: Throwable? = null,
) : Exception(message)
