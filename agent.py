# agent.py
from utils import call_model
from tools import simple_summarize
from memory_bank import MemoryBank

class DocumentSummarizerAgent:
    """
    Agent that summarizes a document. It will call the external model via utils.call_model()
    if an API key is configured; otherwise it falls back to a simple built-in summarizer.
    """

    def __init__(self, use_model_if_available=True):
        self.use_model_if_available = use_model_if_available
        self.memory = MemoryBank()  # persist last summaries, etc.

    def run(self, document_text, session_id=None):
        """
        Produce a concise summary of document_text.
        Attempts to use call_model(); if that raises or returns None, uses simple_summarize().
        Also stores summary in MemoryBank under key -> session:{session_id}:last_summary
        """
        prompt = (
            "You are an expert summarization assistant. Produce a clear, concise summary "
            "of the provided document. Keep it to a few short paragraphs and highlight key points.\n\n"
            f"Document:\n{document_text}\n\nSummary:"
        )

        summary = None

        # Try to call the external model if allowed
        if self.use_model_if_available:
            try:
                out = call_model(prompt)
                if out and isinstance(out, str) and out.strip():
                    summary = out.strip()
            except Exception:
                # swallow and fall back
                summary = None

        # Fallback to a simple local summarizer
        if not summary:
            summary = simple_summarize(document_text, max_sentences=5)

        # Save to memory (if session provided)
        try:
            if session_id:
                self.memory.upsert(f"session:{session_id}:last_summary", {"summary": summary})
        except Exception:
            # memory failure should not stop the user
            pass

        return summary
