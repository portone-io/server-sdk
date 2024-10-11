package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.WebhookNotFoundError
import java.lang.Exception


/** 웹훅 내역이 존재하지 않는 경우 */
public class WebhookNotFoundException(
  cause: WebhookNotFoundError
) : Exception(cause.message) {
}
