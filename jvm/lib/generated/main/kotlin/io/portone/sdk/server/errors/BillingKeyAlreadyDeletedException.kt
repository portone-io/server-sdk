package io.portone.sdk.server.errors

import io.portone.sdk.server.common.BillingKeyAlreadyDeletedError
import java.lang.Exception


/** 빌링키가 이미 삭제된 경우 */
public class BillingKeyAlreadyDeletedException(
  cause: BillingKeyAlreadyDeletedError
) : Exception(cause.message) {
}
