# (generated with --quick)

from typing import Any

click: module
console: module
mock_wikipedia_random_page: Any
pytest: Any
requests: module
runner: Any
test_main_succeeds_in_production_env: Any

def test_main_fails_on_request_error(runner, mock_requests_get) -> None: ...
def test_main_invokes_requests_get(runner, mock_requests_get) -> None: ...
def test_main_prints_message_on_request_error(runner, mock_requests_get) -> None: ...
def test_main_prints_title(runner, mock_requests_get) -> None: ...
def test_main_succeeds(runner, mock_requests_get) -> None: ...
def test_main_uses_en_wikipedia_org(runner, mock_requests_get) -> None: ...
def test_main_uses_specified_language(runner, mock_wikipedia_random_page) -> None: ...
