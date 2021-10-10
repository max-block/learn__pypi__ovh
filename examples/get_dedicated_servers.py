from examples import get_client


def main():
    client = get_client()

    server_names = client.get("/dedicated/server")

    for name in server_names:
        server_info = client.get(f"/dedicated/server/{name}")
        print(server_info)


if __name__ == "__main__":
    main()
