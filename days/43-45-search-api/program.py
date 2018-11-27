import api


def main():
    print("Talk Python Search:")
    search_terms = input("Search:").split()
    try:
        results = api.search(search_terms)
    except api.NoResultsFound:
        print(f"No results found for {' '.join(search_terms)}")
        return
    for i, episode in enumerate(sorted(results, key=lambda r: r["id"])):
        print(f"{i+1}. {episode['id']}: {episode['title']}")


if __name__ == "__main__":
    main()
