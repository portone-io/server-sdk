import asyncio

from portone_server_sdk import PaymentClient, PortOneClient


def test_payment_client_close_closes_sync_client_tree():
    client = PaymentClient(secret="test")

    try:
        assert not client._sync_client.is_closed
        assert not client.billing_key._sync_client.is_closed

        client.close()

        assert client._sync_client.is_closed
        assert client.billing_key._sync_client.is_closed
    finally:
        asyncio.run(client.aclose())


def test_payment_client_aclose_closes_sync_and_async_client_tree():
    client = PaymentClient(secret="test")

    async def close_client():
        await client.aclose()

    asyncio.run(close_client())

    assert client._sync_client.is_closed
    assert client._async_client.is_closed
    assert client.billing_key._sync_client.is_closed
    assert client.billing_key._async_client.is_closed


def test_root_client_context_manager_closes_sync_subclients():
    with PortOneClient(secret="test") as client:
        payment = client.payment
        billing_key = payment.billing_key
        assert not payment._sync_client.is_closed
        assert not billing_key._sync_client.is_closed

    try:
        assert payment._sync_client.is_closed
        assert billing_key._sync_client.is_closed
    finally:
        asyncio.run(client.aclose())


def test_root_client_async_context_manager_closes_sync_and_async_subclients():
    async def use_client():
        async with PortOneClient(secret="test") as client:
            payment = client.payment
            billing_key = payment.billing_key
            assert not payment._sync_client.is_closed
            assert not payment._async_client.is_closed
            assert not billing_key._sync_client.is_closed
            assert not billing_key._async_client.is_closed
        return payment, billing_key

    payment, billing_key = asyncio.run(use_client())

    assert payment._sync_client.is_closed
    assert payment._async_client.is_closed
    assert billing_key._sync_client.is_closed
    assert billing_key._async_client.is_closed
