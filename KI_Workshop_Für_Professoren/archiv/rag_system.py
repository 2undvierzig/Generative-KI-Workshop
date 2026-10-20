import logging
from pathlib import Path
from typing import List, Dict, Optional

from llama_index.core import VectorStoreIndex, Document, StorageContext
from llama_index.core.node_parser import SentenceSplitter
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core import Settings
from llama_index.vector_stores.chroma import ChromaVectorStore
import chromadb

from pdf_processor import PDFProcessor
from config import (
    OLLAMA_BASE_URL,
    LLM_MODEL,
    EMBEDDING_MODEL,
    CHROMA_DB_PATH,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class RAGSystem:
    """RAG-System mit LlamaIndex, Ollama und ChromaDB"""

    def __init__(self) -> None:
        self.pdf_processor = PDFProcessor()
        self._setup_llm_and_embeddings()
        self._setup_vector_store()
        self.index: Optional[VectorStoreIndex] = None
        self.query_engine = None

    def _setup_llm_and_embeddings(self) -> None:
        self.llm = Ollama(
            model=LLM_MODEL,
            base_url=OLLAMA_BASE_URL,
            temperature=0.1,
            request_timeout=120.0,
        )

        self.embed_model = OllamaEmbedding(
            model_name=EMBEDDING_MODEL,
            base_url=OLLAMA_BASE_URL,
            ollama_additional_kwargs={"mirostat": 0},
        )

        Settings.llm = self.llm
        Settings.embed_model = self.embed_model
        Settings.text_splitter = SentenceSplitter(chunk_size=1024, chunk_overlap=20)  # ersetzt node_parser

        logger.info("LLM und Embeddings konfiguriert")

    def _setup_vector_store(self) -> None:
        chroma_client = chromadb.PersistentClient(path=str(CHROMA_DB_PATH))
        collection = chroma_client.get_or_create_collection("documents")
        self.vector_store = ChromaVectorStore(chroma_collection=collection)
        self.storage_context = StorageContext.from_defaults(vector_store=self.vector_store)
        logger.info("Vector Store eingerichtet")

    def process_and_index_documents(self) -> None:
        processed = self.pdf_processor.process_all_pdfs()
        if not processed:
            logger.warning("Keine Dokumente zum Indizieren")
            return

        docs = [
            Document(
                text=doc["text"],
                metadata={
                    "source": doc["source_file"],
                    "processed_file": doc["output_file"],
                },
            )
            for doc in processed
        ]

        self.index = VectorStoreIndex.from_documents(
            docs, storage_context=self.storage_context
        )
        self.query_engine = self.index.as_query_engine(
            similarity_top_k=3, response_mode="compact"
        )
        logger.info("Index und Query Engine erstellt")

    def _load_existing_index(self) -> bool:
        if CHROMA_DB_PATH.exists():
            self.index = VectorStoreIndex.from_vector_store(
                self.vector_store, storage_context=self.storage_context
            )
            self.query_engine = self.index.as_query_engine(
                similarity_top_k=3, response_mode="compact"
            )
            logger.info("Index geladen")
            return True
        return False

    def initialize(self, force_reindex: bool = False) -> None:
        if not force_reindex and self._load_existing_index():
            return
        self.process_and_index_documents()

    def query(self, question: str) -> str:
        if not self.query_engine:
            raise RuntimeError("Index fehlt – zuerst initialize() ausführen")
        system_prompt = (
            "Du bist ein hilfreicher Assistent, der Fragen zu Programmierung und "
            "Informatik beantwortet. Antworte auf Deutsch und stütze dich auf den Kontext."
        )
        full_query = f"{system_prompt}\n\nFrage: {question}"
        return str(self.query_engine.query(full_query))
