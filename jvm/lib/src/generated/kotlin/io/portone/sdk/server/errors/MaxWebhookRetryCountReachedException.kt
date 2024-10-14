package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.MaxWebhookRetryCountReachedError
import java.lang.Exception


/** 동일한 webhook id에 대한 수동 재시도 횟수가 최대에 도달한 경우 */
public class MaxWebhookRetryCountReachedException(
  cause: MaxWebhookRetryCountReachedError
) : Exception(cause.message) {
}
