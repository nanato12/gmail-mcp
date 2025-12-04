"""
main.py - Gmail MCP Serverエントリーポイント
"""
import os

from dotenv import load_dotenv

from server import create_server, init_gmail_credentials

# 環境変数のロード
load_dotenv()


def main():
    """メイン実行関数"""
    # Gmail認証
    init_gmail_credentials()

    # トランスポート設定
    transport = os.getenv("TRANSPORT", "stdio")
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", "3001"))

    # サーバー作成（host/portはFastMCP初期化時に設定）
    server = create_server(host=host, port=port)

    # サーバー起動
    print(f"[INFO] Starting Gmail MCP server with {transport} transport...")

    if transport == "http":
        server.run(transport="streamable-http")
    else:
        server.run(transport="stdio")


if __name__ == "__main__":
    main()