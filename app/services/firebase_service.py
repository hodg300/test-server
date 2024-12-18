import json
import os

import firebase_admin
from dotenv import load_dotenv
from firebase_admin import credentials, firestore
from typing import Dict, Any, List


class FirebaseService:
    def __init__(self):
        # Initialize Firebase app
        load_dotenv()

        firebase_credentials_json = os.getenv("FIREBASE_ADMIN_KEY")
        print(f"{firebase_credentials_json=}")
        if firebase_credentials_json:
            cred = credentials.Certificate(
                json.loads(firebase_credentials_json))
            firebase_admin.initialize_app(cred)

        else:
            cred = credentials.Certificate("/Users/hodgohasi/PycharmProjects/test-server/firebase-credentials.json")
            firebase_admin.initialize_app(cred)
        # cred = credentials.Certificate("/Users/hodgohasi/PycharmProjects/test-server/firebase-credentials.json")
        # firebase_admin.initialize_app(cred)
        # Initialize Firestore client
        self.db = firestore.client()




    def save_data_to_firestore(self, collection: str, document_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Save data to a Firestore collection.

        Args:
            collection (str): The name of the Firestore collection.
            document_id (str): The ID of the document.
            data (Dict[str, Any]): The data to be saved.

        Returns:
            Dict[str, Any]: The saved document data.
        """
        doc_ref = self.db.collection(collection).document(document_id)
        doc_ref.set(data)
        return {"id": document_id, "data": data}

    def fetch_data_from_firestore(self, collection: str, document_id: str) -> Dict[str, Any]:
        """
        Fetch data from a Firestore collection.

        Args:
            collection (str): The name of the Firestore collection.
            document_id (str): The ID of the document.

        Returns:
            Dict[str, Any]: The fetched document data.
        """
        doc_ref = self.db.collection(collection).document(document_id)
        doc = doc_ref.get()
        if doc.exists:
            return doc.to_dict()
        else:
            return {"error": "Document not found"}

    def fetch_all_docs_from_firestore(self, collection: str, limit=100) -> List[Dict[str, Any]]:
        """
        Fetch all documents from a Firestore collection.

        Args:
            collection (str): The name of the Firestore collection.

        Returns:
            List[Dict[str, Any]]: A list of all documents' data.
        """
        docs_ref = self.db.collection(collection).order_by("date", direction="DESCENDING").limit(limit)
        docs = docs_ref.stream()  # This gets all documents in the collection

        all_documents = []
        for doc in docs:
            all_documents.append(doc.to_dict())  # Convert doc to dict and append to list

        return all_documents
