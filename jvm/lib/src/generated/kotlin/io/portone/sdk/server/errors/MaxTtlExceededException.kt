package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.MaxTtlExceededError
import java.lang.Exception


/** 요청된 TTL이 정책 상한을 초과한 경우 */
public class MaxTtlExceededException internal constructor(
  cause: MaxTtlExceededError
) : PortOneException(cause.message), CreatePaymentSessionException {
}
