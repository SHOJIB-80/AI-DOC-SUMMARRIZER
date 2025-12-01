from agent import DocumentSummarizerAgent

def main():
    print("=== AI Document Summarizer Agent ===")
    print("Paste your document text below. When finished, type: END\n")

    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)

    document = "\n".join(lines)

    agent = DocumentSummarizerAgent()
    summary = agent.run(document)

    print("\n--- SUMMARY ---\n")
    print(summary)
    print("\n--- END ---")

if __name__ == "__main__":
    main()