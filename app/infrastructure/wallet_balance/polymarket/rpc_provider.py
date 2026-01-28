from typing import Callable

from web3 import Web3, HTTPProvider


class RpcProvider[T]:
    def __init__(self, rpc_urls: list[str], timeout: int = 5):
        self._rpc_urls = rpc_urls
        self._timeout = timeout

    def execute(self, call: Callable[[Web3], T]) -> T:
        last_error: Exception | None = None

        for index, url in enumerate(self._rpc_urls):
            try:
                web3 = Web3(
                    HTTPProvider(url, request_kwargs={"timeout": self._timeout})
                )

                result = call(web3)

                if index != 0:
                    self._rpc_urls.insert(0, self._rpc_urls.pop(index))

                return result

            except Exception as e:
                last_error = e
                continue

        raise RuntimeError("All RPCs failed") from last_error