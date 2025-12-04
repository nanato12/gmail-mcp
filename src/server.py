"""
server.py - Gmail MCPサーバー設定と初期化
"""
import os
from pathlib import Path

from mcp.server.fastmcp import FastMCP

import utils.gmail_utils as gmail_utils
from tools import (
    # 読み取り専用ツールのみインポート（送信・削除は無効化）
    # send_email,  # 無効化
    # create_draft,  # 無効化
    read_email,
    search_emails,
    # delete_email,  # 無効化
    modify_label,
    create_label_tool,
    delete_label_tool,
    list_labels_tool,
    get_or_create_label_tool,
    update_label_tool,
    find_label_by_name_tool,
)

# 設定
BASE_DIR = Path(__file__).resolve().parent.parent
CREDENTIALS_DIR = BASE_DIR / "credentials"
OAUTH_KEYS = os.getenv(
    "GMAIL_OAUTH_PATH", str(CREDENTIALS_DIR / "client_secret_gmail_oauth.json")
)
CRED_PATH = os.getenv(
    "GMAIL_CREDENTIALS_PATH", str(CREDENTIALS_DIR / "credentials.json")
)
# 読み取り専用スコープに変更
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


def create_server(host: str = "127.0.0.1", port: int = 3001) -> FastMCP:
    """MCP サーバーの作成とツール登録（読み取り専用）

    Args:
        host: サーバーホスト（デフォルト: 127.0.0.1）
        port: サーバーポート（デフォルト: 3001）
    """
    server = FastMCP("gmail", host=host, port=port)

    # 読み取り専用ツールのみ登録
    # server.tool()(send_email)  # 無効化
    # server.tool()(create_draft)  # 無効化
    server.tool()(read_email)
    server.tool()(search_emails)
    # server.tool()(delete_email)  # 無効化
    server.tool()(modify_label)
    server.tool()(create_label_tool)
    server.tool()(delete_label_tool)
    server.tool()(list_labels_tool)
    server.tool()(get_or_create_label_tool)
    server.tool()(update_label_tool)
    server.tool()(find_label_by_name_tool)

    return server

def init_gmail_credentials():
    """Gmail認証を行う"""
    gmail_utils.load_credentials(
        config_path=BASE_DIR,
        cred_path=CRED_PATH,
        oauth_path=OAUTH_KEYS,
        scopes=SCOPES
    )