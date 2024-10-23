package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2BCannotChangeTaxTypeError
import java.lang.Exception


/** 세금계산서 과세 유형을 수정할 수 없는 경우 */
public class B2BCannotChangeTaxTypeException(
  cause: B2BCannotChangeTaxTypeError
) : Exception(cause.message) {
}
