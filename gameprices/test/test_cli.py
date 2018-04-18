from gameprices.cli.cli import eshop_main
from gameprices.cli.cli import psn_main
from gameprices.shops.eshop import Eshop
from gameprices.shops.psn import Psn
import sys
import pytest

def test_cli_search():
    sys.argv = [
        "eshopcli",
        "--query",
        "'Vostok'"
    ]

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        eshop_main()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

def test_cli_by_id_and_whish_price_not_matched():
    sys.argv = [
        "eshopcli",
        "--id",
        "DE/de###1173281###Mario_Kart_8_Deluxe",
        "--price",
        "1"
    ]

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        eshop_main()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == -1 

def test_cli_by_id_and_whish_price_matched():
    sys.argv = [
        "eshopcli",
        "--id",
        "DE/de###1173281###Mario_Kart_8_Deluxe",
        "--price",
        "100"
    ]

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        eshop_main()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

def test_cli_by_container():
    sys.argv = [
        "psncli",
        "--container",
        "STORE-MSF75508-PRICEDROPSCHI"
    ]

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        psn_main()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

def test_cli_no_match():
    sys.argv = [
        "psncli",
        "--query",
        "sdfjsdkfsdkfjskdfj YOU WONT FIND ME NEVER EVER. HOPEFULLY"
    ]

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        psn_main()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == -1 