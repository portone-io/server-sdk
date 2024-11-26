from __future__ import annotations
from typing import Any, Optional, Union
from ...payment.payment_schedule.failed_payment_schedule import FailedPaymentSchedule, _deserialize_failed_payment_schedule, _serialize_failed_payment_schedule
from ...payment.payment_schedule.pending_payment_schedule import PendingPaymentSchedule, _deserialize_pending_payment_schedule, _serialize_pending_payment_schedule
from ...payment.payment_schedule.revoked_payment_schedule import RevokedPaymentSchedule, _deserialize_revoked_payment_schedule, _serialize_revoked_payment_schedule
from ...payment.payment_schedule.scheduled_payment_schedule import ScheduledPaymentSchedule, _deserialize_scheduled_payment_schedule, _serialize_scheduled_payment_schedule
from ...payment.payment_schedule.started_payment_schedule import StartedPaymentSchedule, _deserialize_started_payment_schedule, _serialize_started_payment_schedule
from ...payment.payment_schedule.succeeded_payment_schedule import SucceededPaymentSchedule, _deserialize_succeeded_payment_schedule, _serialize_succeeded_payment_schedule

PaymentSchedule = Union[FailedPaymentSchedule, PendingPaymentSchedule, RevokedPaymentSchedule, ScheduledPaymentSchedule, StartedPaymentSchedule, SucceededPaymentSchedule, dict]
"""결제 예약 건
"""


def _serialize_payment_schedule(obj: PaymentSchedule) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, FailedPaymentSchedule):
        return _serialize_failed_payment_schedule(obj)
    if isinstance(obj, PendingPaymentSchedule):
        return _serialize_pending_payment_schedule(obj)
    if isinstance(obj, RevokedPaymentSchedule):
        return _serialize_revoked_payment_schedule(obj)
    if isinstance(obj, ScheduledPaymentSchedule):
        return _serialize_scheduled_payment_schedule(obj)
    if isinstance(obj, StartedPaymentSchedule):
        return _serialize_started_payment_schedule(obj)
    if isinstance(obj, SucceededPaymentSchedule):
        return _serialize_succeeded_payment_schedule(obj)


def _deserialize_payment_schedule(obj: Any) -> PaymentSchedule:
    try:
        return _deserialize_failed_payment_schedule(obj)
    except Exception:
        pass
    try:
        return _deserialize_pending_payment_schedule(obj)
    except Exception:
        pass
    try:
        return _deserialize_revoked_payment_schedule(obj)
    except Exception:
        pass
    try:
        return _deserialize_scheduled_payment_schedule(obj)
    except Exception:
        pass
    try:
        return _deserialize_started_payment_schedule(obj)
    except Exception:
        pass
    try:
        return _deserialize_succeeded_payment_schedule(obj)
    except Exception:
        pass
    return obj
